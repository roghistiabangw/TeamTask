# === Stage 50: Add unit tests for import and export behavior ===
# Project: TeamTask
import json, os, tempfile, unittest

class TestTeamTaskIOTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, 'tasks.json')
    
    def tearDown(self):
        try:
            os.remove(self.test_file)
            os.rmdir(self.temp_dir)
        except OSError:
            pass

    def test_export_empty_tasks(self):
        from team_task import TeamTaskBoard
        board = TeamTaskBoard()
        data = board.export_to_json()
        self.assertEqual(data, [])

    def test_import_valid_data(self):
        from team_task import TeamTaskBoard
        sample_data = [
            {'id': 1, 'title': 'Fix bug', 'owner': 'Alice', 'priority': 'high'},
            {'id': 2, 'title': 'Write docs', 'owner': 'Bob', 'priority': 'low'}
        ]
        with open(self.test_file, 'w') as f:
            json.dump(sample_data, f)

        board = TeamTaskBoard()
        imported_tasks = board.import_from_json(self.test_file)
        
        self.assertEqual(len(imported_tasks), 2)
        self.assertEqual(imported_tasks[0]['title'], 'Fix bug')
        self.assertEqual(imported_tasks[1]['owner'], 'Bob')

    def test_export_with_data(self):
        from team_task import TeamTaskBoard
        board = TeamTaskBoard()
        board.add_task('Review PR', owner='Charlie', priority='medium')
        
        data = board.export_to_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Review PR')

    def test_import_invalid_file(self):
        from team_task import TeamTaskBoard
        with open(self.test_file, 'w') as f:
            f.write('not valid json {{{')
        
        board = TeamTaskBoard()
        imported_tasks = board.import_from_json(self.test_file)
        self.assertEqual(imported_tasks, [])

    def test_roundtrip_import_export(self):
        from team_task import TeamTaskBoard
        initial_data = [
            {'id': 10, 'title': 'Initial Task', 'owner': 'Dave', 'priority': 'critical'}
        ]
        
        with open(self.test_file, 'w') as f:
            json.dump(initial_data, f)

        board1 = TeamTaskBoard()
        imported = board1.import_from_json(self.test_file)
        
        exported = board1.export_to_json()
        self.assertEqual(exported, initial_data)
