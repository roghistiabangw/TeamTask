# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: TeamTask
from unittest.mock import patch, MagicMock
import sys
sys.path.insert(0, '.')
from task_board import TaskBoard

def test_update_task_with_invalid_priority():
    board = TaskBoard()
    with patch('builtins.input', return_value='1'):
        result = board.update_task(task_id=1, priority='invalid')
        assert result['status'] == 'error'
        assert 'priority must be 1-3' in result['message']

def test_delete_nonexistent_task():
    board = TaskBoard()
    with patch('builtins.input', return_value='y'):
        result = board.delete_task(task_id=999)
        assert result['status'] == 'error'
        assert 'Task not found' in result['message']

def test_update_task_with_empty_notes():
    board = TaskBoard()
    with patch('builtins.input', return_value='1'):
        result = board.update_task(task_id=1, notes='')
        assert result['status'] == 'success'
