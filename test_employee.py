from employee import employee_Details


def test_employee_Details():
    result = employee_Details("JohnDoe", 30, "IT","50000")

    expected= "name: JohnDoe\nEmployee ID: 30\nDepartment: IT\nsalary: 50000"

    assert result == expected
