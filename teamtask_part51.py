# === Stage 51: Add unit tests for search and filter behavior ===
# Project: TeamTask
import unittest
from team_task import Task, TeamTaskBoard

class TestSearchFilter(unittest.TestCase):
    def setUp(self):
        self.board = TeamTaskBoard()
    
    def test_filter_by_owner(self):
        t1 = Task("Fix bug", "Alice", 3)
        t2 = Task("New feature", "Bob", 1)
        self.board.add_task(t1)
        self.board.add_task(t2)
        filtered = self.board.filter_tasks(owner="Alice")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Fix bug")

    def test_filter_by_priority(self):
        t1 = Task("Urgent fix", "Alice", 3)
        t2 = Task("Nice to have", "Bob", 1)
        self.board.add_task(t1)
        self.board.add_task(t2)
        filtered = self.board.filter_tasks(priority=3)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "Urgent fix")

    def test_filter_by_priority_range(self):
        t1 = Task("High", "Alice", 3)
        t2 = Task("Medium", "Bob", 2)
        t3 = Task("Low", "Charlie", 1)
        self.board.add_task(t1)
        self.board.add_task(t2)
        self.board.add_task(t3)
        filtered = self.board.filter_tasks(priority_range=(2, 4))
        self.assertEqual(len(filtered), 2)

    def test_search_by_title(self):
        t1 = Task("Fix login bug", "Alice", 3)
        t2 = Task("Update docs", "Bob", 1)
        self.board.add_task(t1)
        self.board.add_task(t2)
        filtered = self.board.search_tasks(query="login")
        self.assertEqual(len(filtered), 1)

    def test_search_case_insensitive(self):
        t1 = Task("Fix Login Bug", "Alice", 3)
        self.board.add_task(t1)
        filtered = self.board.search_tasks(query="LOGIN")
        self.assertEqual(len(filtered), 1)
