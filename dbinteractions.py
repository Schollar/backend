import dbhelpers


def make_line(content):
    line_id = dbhelpers.run_insert_statement(
        "INSERT INTO line(content) VALUES (?)", [content])
    if(line_id == None):
        return None, False
    else:
        return line_id, True


def get_lines():
    lines = dbhelpers.run_select_statement(
        "SELECT content, created_at, id FROM line", [])
    if(lines == None):
        return None, False
    else:
        return lines, True
