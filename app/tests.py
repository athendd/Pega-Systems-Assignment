"""
Tests each API route and service to ensure that they work as intended 
"""

from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

@pytest.fixture(scope="class")
def shared_item_id():
    """Returns the ID of the last item for use in other tests."""
    all_items = client.get('/items/')
    last_item_id = all_items.json()[len(all_items.json()) - 1]['id']

    return last_item_id

class TestAPIRoutes:

    def test_create_item(self):
        """Test the create new item route."""
        new_item = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'read': True}
        response = client.post(f'/items/', json = new_item)

        assert response.status_code == 200

    def test_create_item_no_title(self):
        """Test that create item fails when no title is given."""
        new_item = {'author': 'F. Scott Fitzgerald', 'read': True}
        response = client.post(f'/items/', json = new_item)

        assert response.status_code == 422

    def test_create_item_no_author(self):
        """Test that create item fails when no author is given."""
        new_item = {'title': 'The Great Gatsby', 'read': True}
        response = client.post(f'/items/', json = new_item)

        assert response.status_code == 422

    def test_create_item_no_read(self):
        """Test that create item fails when no read is given."""
        new_item = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}
        response = client.post(f'/items/', json = new_item)

        assert response.status_code == 422

    def test_get_all_items(self):
        """Test the get all items route with pagination."""
        response = client.get('/items/')

        assert response.status_code == 200

    def test_pagination_all_items(self):
        """Test the get all items route with pagination."""
        response = client.get('/items/?page=1&page_size=10')

        assert response.status_code == 200

    def test_get_item(self, shared_item_id):
        """Test the get item by id route."""
        response = client.get(f'/items/{shared_item_id}')

        assert response.status_code == 200

    def test_get_item_to_fail(self, shared_item_id):
        """Test that /items/{item_id} fails when invalid id given."""
        response = client.get(f'/items/{shared_item_id + 1}')

        assert response.status_code == 404

    def test_update_item(self, shared_item_id):
        """Test the update item route."""
        updated_data = {"title": "The Great Gatsby - Special Edition"}
        response = client.put(f'/items/{shared_item_id}', json = updated_data)

        assert response.status_code == 200

    def test_delete_item(self, shared_item_id):
        """Test the delete item route."""
        response = client.delete(f'/items/{shared_item_id}')

        assert response.status_code == 200

