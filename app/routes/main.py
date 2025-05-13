from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, url_prefix='/')


@main_bp.route('/')
def f():
    return render_template('index.html')


@main_bp.route('/about.html')
def about():
    return render_template('about.html')


@main_bp.route('/index.html')
def index():
    return render_template('index.html')


@main_bp.route('/shop-3-column.html')
def shops():
    return render_template('shop-3-column.html')


@main_bp.route('/my-account.html')
def account():
    return render_template('my-account.html')


@main_bp.route('/login.html')
def login():
    return render_template('login.html')


@main_bp.route('/404.html')
def four_zero_four():
    return render_template('404.html')


@main_bp.route('/privacy-policy.html')
def privacy_policy():
    return render_template('privacy-policy.html')


@main_bp.route('/shop-right-sidebar.html')
def shop():
    return render_template('shop-right-sidebar.html')


@main_bp.route('/contact.html')
def contact():
    return render_template('contact.html')


@main_bp.route('/wishlist.html')
def wishlist():
    return render_template('wishlist.html')
