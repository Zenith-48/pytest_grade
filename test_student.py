from student import process_student_data

def test_default_values():
    result = process_student_data(["student.py"])

    assert result["name"] == "Shalina Maniyar"
    assert result["department"] == "BCA"
    assert result["semester"] == "3"
    assert result["total"] == 283
    assert result["grade"] == "A"


def test_command_line_arguments():
    args = [
        "student.py",
        "Aarav",
        "BCA",
        "3",
        "70",
        "75",
        "80"
    ]

    result = process_student_data(args)

    assert result["name"] == "Aarav"
    assert result["total"] == 225
    assert result["average"] == 75
    assert result["grade"] == "C"