CATEGORIES = ["Food", "Transport", "Going out", "Shopping", "Bills", "Course costs", "Other"]


def money(amount):
    pass


def read_money(text):
    pass


def check_amount(text, biggest):
    pass


def check_spending(amount_text, category, spent_on, today):
    pass


def clean_username(username):
    """This tidies the username, removes spaces at the ends and use small letters."""
    return username.strip().lower()


def check_new_account(username, password, password_again, taken_usernames):
    """Check the create an account form, gives back a list of problems."""
    problems = []
    username = clean_username(username)
    if len(username) < 3 or len(username) > 20 or not username.isalnum():
        problems.append("Your username must be 3 to 20 letters and numbers with no spaces.")
    elif username in taken_usernames:
        problems.append("That username is already taken, please choose another one.")
    if len(password) < 8:
        problems.append("Your password must be at least 8 characters long.")
    elif password != password_again:
        problems.append("The two passwords are not the same.")
    return problems


def hash_password(password):
    """Srambling password with SHA-256, so the real password is never saved anywhere."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def week_start(today):
    pass


def spending_this_week(spending, today):
    pass


def total(spending):
    pass


def totals_by_category(spending):
    pass


def budget_status(spent, weekly_budget):
    pass
