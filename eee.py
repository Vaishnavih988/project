class Volunteer:
    def __init__(self, volunteer_id, name, skills):
        self.volunteer_id = volunteer_id
        self.name = name
        self.skills = skills

class EventManager:
    def __init__(self):
        self.volunteers = {}

    def add_volunteer(self, volunteer_id, name, skills):
        if volunteer_id in self.volunteers:
            raise ValueError("Volunteer ID already exists")
        self.volunteers[volunteer_id] = Volunteer(volunteer_id, name, skills)

    def get_volunteer(self, volunteer_id):
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer ID does not exist")
        return self.volunteers[volunteer_id]

    def update_volunteer(self, volunteer_id, name=None, skills=None):
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer ID does not exist")
        volunteer = self.volunteers[volunteer_id]
        if name:
            volunteer.name = name
        if skills:
            volunteer.skills = skills

    def delete_volunteer(self, volunteer_id):
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer ID does not exist")
        del self.volunteers[volunteer_id]

    '''def manage_volunteers_for_events(self, event_id):
        # Implementation to manage and schedule volunteers for events goes here
        pass'''

'''class HoursTracker:
    def __init__(self):
        self.hours_data = {}

    def track_volunteer_hours(self, hours_data):
        # Implementation to track and validate volunteer hours goes here
        pass'''

# Unit tests
import unittest

class TestEventManager(unittest.TestCase):
    def setUp(self):
        self.event_manager = EventManager()
        self.event_manager.add_volunteer(1, "John Doe", "football")
        self.event_manager.add_volunteer(2, "Jane Smith", "cricket")

    def test_add_volunteer(self):
        self.event_manager.add_volunteer(3, "Alice Johnson", "basketball")
        self.assertIn(3, self.event_manager.volunteers)

    def test_get_volunteer(self):
        volunteer = self.event_manager.get_volunteer(1)
        self.assertEqual(volunteer.name, "John Doe")

    def test_update_volunteer(self):
        self.event_manager.update_volunteer(1, name="Johnathan Doe")
        volunteer = self.event_manager.get_volunteer(1)
        self.assertEqual(volunteer.name, "Johnathan Doe")

    def test_delete_volunteer(self):
        self.event_manager.delete_volunteer(1)
        self.assertNotIn(1, self.event_manager.volunteers)

if __name__ == '__main__':
    unittest.main(verbosity=3)



