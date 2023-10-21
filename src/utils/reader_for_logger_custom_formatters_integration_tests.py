def get_last_log_line_for_integration_test_assertion(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        last_seven_lines = ''.join(lines[-1:])
        return lines[-1] if lines else ''
