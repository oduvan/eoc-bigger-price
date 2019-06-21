"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [2, [
                {"name": "bread", "price": 100},
                {"name": "wine", "price": 138},
                {"name": "meat", "price": 15},
                {"name": "water", "price": 1}
            ]],
            "answer": [
                {"name": "wine", "price": 138},
                {"name": "bread", "price": 100}
            ]
        },
        {
            "input": [1, [
                {"name": "pen", "price": 5},
                {"name": "whiteboard", "price": 170}
            ]],
            "answer": [{"name": "whiteboard", "price": 170}]
        }
    ],
    "Extra": [
        {
            "input": [2, [
                {"name": "bread", "price": 10},
                {"name": "wine", "price": 138},
                {"name": "meat", "price": 15},
                {"name": "milk", "price": 25}
            ]],
            "answer": [
                {"name": "wine", "price": 138},
                {"name": "milk", "price": 25}
            ]
        }
    ]
}
