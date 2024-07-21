from flask import Blueprint, render_template, redirect, url_for, request
from flask_security import login_required
from app.forms.DebtorForm import DebtorForm
from extensions.alchemy import db
from app.entities.models import Debtor

debtor_bp = Blueprint('debtor', __name__, url_prefix="/debtors")

@debtor_bp.route('/', methods=["POST", "GET"])
@login_required
def index():
    debtors = Debtor.query.all();
    return render_template('debtor/index.html', debtors=debtors)

@debtor_bp.route('/create', methods=["POST", "GET"])
@login_required
def create():
    form = DebtorForm()
    if request.method == 'GET':
        return render_template('debtor/create.html', form=form)
    if not form.validate_on_submit():
        return render_template('debtor/create.html', form=form)
    new_debtor = Debtor(name=form.name.data)
    db.session.add(new_debtor)
    db.session.commit()
    return redirect(url_for("main.home"))


@debtor_bp.route('/modal/create', methods=["POST"])
@login_required
def modal_create():
    form = DebtorForm()
    if not form.validate_on_submit():
        return render_template('debtor/_modal-create.html', form_search=form)
    new_debtor = Debtor(name=form.name.data)
    db.session.add(new_debtor)
    db.session.commit()
    return render_template(
        'debtor/_modal-create.html', 
        form_search=form,
        message='¡Nuevo deudor añadido!'
    )


@debtor_bp.route('/search', methods=["POST"])
@login_required
def search():
    form = DebtorForm()
    form.validate_on_submit()
    name = form.name.data
    query = Debtor.query.filter(Debtor.name.ilike(f'%{name}%'))
    debtors = query.all()
    return render_template("debtor/_list-items.html", debtors=debtors)
