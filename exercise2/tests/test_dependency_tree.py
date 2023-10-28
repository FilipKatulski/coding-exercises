import unittest

from dependencytrees.dependency_tree_creator import create_dependency_tree


class TestDependencyTree(unittest.TestCase):
    def test_create_dependency_tree(self):
        # Test with example1.json
        expected_output = """- pkg1\n  - pkg2\n    - pkg3\n  - pkg3\n- pkg2\n  - pkg3\n- pkg3"""
        self.assertEqual(str(create_dependency_tree("examples/example1.json")), expected_output)

        # Test with example2.json
        expected_output = "- pkg1\n  - pkg2\n    - pkg3\n    - pkg4\n      - pkg5\n  - pkg3\n  - pkg4\n    - pkg5\n- pkg2\n  - pkg3\n  - pkg4\n    - pkg5\n- pkg3\n- pkg4\n  - pkg5\n- pkg5"
        self.assertEqual(str(create_dependency_tree("examples/example2.json")), expected_output)

        # Test with example3.json
        expected_output = "- pkg1\n  - pkg2\n    - pkg3\n      - pkg4\n        - pkg5\n          - pkg6\n- pkg2\n  - pkg3\n    - pkg4\n      - pkg5\n        - pkg6\n- pkg3\n  - pkg4\n    - pkg5\n      - pkg6\n- pkg4\n  - pkg5\n    - pkg6\n- pkg5\n  - pkg6"
        self.assertEqual(str(create_dependency_tree("examples/example3.json")), expected_output)

if __name__ == '__main__':
    unittest.main()
