from flask import Blueprint, render_template, redirect, url_for, request
from flask_security import login_required
from app.forms.DebtForm import DebtForm, DebtEditForm
from app.forms.DebtorForm import DebtorForm
from app.forms.payments import PaymentCreateForm

from app.entities.models import Debt
from app.services import DebtService

debt_bp = Blueprint('debts', __name__, url_prefix="/debts")
debts_service = DebtService()


@debt_bp.route('/', methods=["GET"])
@login_required
def index():
    debts = Debt.query.all()
    return render_template('debts/index.html', debts=debts)


@debt_bp.route('/create', methods=["POST", "GET"])
@login_required
def create():
    form = DebtForm()
    form_debtor_search = DebtorForm()
    debts_service.form_feed_choices(form)

    if request.method == 'GET':
        return render_template('debts/create.html',
            form=form,
            form_search=form_debtor_search,
        )
    if not form.validate_on_submit():
        return render_template('debts/create.html',
            form=form,
            form_search=form_debtor_search,
        )

    debt_values = form.data
    debts_service.standardize_value(debt_values)
    debts_service.create_debt(debt_values)
    return redirect(url_for("debts.index"))


@debt_bp.route('/edit/<int:debt_id>', methods=["POST", "GET"])
@login_required
def edit(debt_id: int):
    debt = Debt.query.get_or_404(debt_id)
    form = DebtEditForm()
    form_payment = PaymentCreateForm()
    debts_service.form_feed_choices(form)
    debts_service.form_feed_choices(form_payment)


    if request.method == 'GET':
        form.process(obj=debt)
        return render_template('debts/edit.html',
            form=form,
            debt=debt,
            form_payment=form_payment
        )
    
    if not form.validate_on_submit():
        return render_template('debts/edit.html',
            form=form,
            debt=debt,
            form_payment=form_payment
        )

    debt_values = form.data
    debts_service.standardize_value(debt_values)
    debts_service.edit_debt(debt, debt_values)
    return redirect(url_for("debts.index"))


@debt_bp.route('/<int:debt_id>/payment', methods=["POST"])
@login_required
def payment(debt_id: int):
    debt = Debt.query.get_or_404(debt_id)
    form = PaymentCreateForm()
    payment_values = form.data
    debts_service.save_original_value(payment_values)
    debts_service.standardize_value(payment_values)
    debts_service.save_payment(payment_values, debt)


@debt_bp.route('/view/<int:debt_id>', methods=["POST", "GET"])
@login_required
def view(debt_id: int):
    debt = Debt.query.get_or_404(debt_id)
    return render_template('debts/view.html', debt=debt)