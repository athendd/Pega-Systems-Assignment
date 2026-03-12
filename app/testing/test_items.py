"""
Runs unit tests for application.
"""

from testing.test_db import *
from main import app
from fastapi.testclient import TestClient
import pytest

client = TestClient(app)

@pytest.fixture(scope="function")
def shared_item():
    """Returns the ID of the last item for use in other tests."""
    new_item = {
        'title': 'Book Name',
        'author': 'Chosen author',
        'read': False
    }

    response = client.post('/items/', json = new_item)
    
    return response.json()

class TestAPIRoutes:

    def test_create_item(self):
        """Test the create new item route."""
        new_item = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'notes': 'Good book', 'read': True}
        response = client.post(f'/items/', json = new_item)

        assert response.status_code == 200

        data = response.json()

        assert data['title'] == 'The Great Gatsby'
        assert data['author'] == 'F. Scott Fitzgerald'
        assert data['notes'] == 'Good book'
        assert data['read'] is True

    def test_create_item_no_title(self):
        """Test that create item fails when no title is given."""
        new_item = {'author': 'F. Scott Fitzgerald', 'read': True}
        response = client.post(f'/items/', json = new_item)

        assert response.status_code == 422

    def test_create_item_empty_title(self):
        """Test that create item fails when title has no value."""
        new_item = {'title': '', 'author': 'F. Scott Fitzgerald', 'read': True}
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

    def test_create_item_invalid_read(self):
        """Test that create item fails when invalid value is given to read attribute"""
        new_item = {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'read': 'None'}
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

    def test_pagination_structure(self):
        """Test the pagination metadata to ensure it is all there"""
        response = client.get('/items/?page=1&page_size=5')
        data = response.json()

        assert 'items' in data
        assert 'total' in data
        assert 'page' in data
        assert 'total_pages' in data

    def test_get_item(self, shared_item):
        """Test the get item by id route."""
        response = client.get(f'/items/{shared_item['id']}')

        assert response.status_code == 200

    def test_update_item(self, shared_item):
        """Test the update item route."""
        updated_data = {"title": "The Great Gatsby - Special Edition", 'read': False}
        response = client.put(f'/items/{shared_item['id']}', json = updated_data)
        data = response.json()

        assert response.status_code == 200

        assert data['read'] is False
        assert data['title'] == 'The Great Gatsby - Special Edition'


    def test_delete_item(self, shared_item):
        """Test the delete item route."""
        response = client.delete(f'/items/{shared_item['id']}')

        assert response.status_code == 200

    def test_get_item_to_fail(self, shared_item):
        """Test that /items/{item_id} fails when invalid id given."""
        response = client.get(f'/items/{shared_item['id'] + 1}')

        assert response.status_code == 404

    def test_invalid_page(self):
        """Test page restrictions for pagination"""
        response = client.get('/items/?page=0')

        assert response.status_code == 422

    def test_invalid_page_size(self):
        """Test that page_size cannot exceed 100."""
        response = client.get('/items/?page_size=1000')

        assert response.status_code == 422

    def test_created_at_exists(self, shared_item):
        assert 'created_at' in shared_item