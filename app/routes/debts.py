from flask import Blueprint, render_template, redirect, url_for, request
from flask_security import login_required
from app.forms.DebtForm import DebtForm
from app.forms.DebtorForm import DebtorForm
from app.entities.models import Debt, Currency
from app.entities.models import Debtor
from app.services import DebtService, CurrencyService

debt_bp = Blueprint('debts', __name__, url_prefix="/debts")
debts_service = DebtService()


@debt_bp.route('/', methods=["GET"])
@login_required
def index():
    debtors = Debtor.query.all();
    debtors = debts_service.get_debtors_debts(debtors)
    return render_template('debts/index.html', debtors=debtors)


@debt_bp.route('/create', methods=["POST", "GET"])
@login_required
def create():
    form = DebtForm()
    form_debtor_search = DebtorForm()

    currencies = [
        (currency.id, currency.name)
        for currency
        in Currency.query.all()
    ]
    form.set_currencies(currencies)

    if request.method == 'GET':
        return render_template('debts/create.html',
            form=form,
            form_search=form_debtor_search
        )
    if not form.validate_on_submit():
        return render_template('debts/create.html',
            form=form,
            form_search=form_debtor_search
        )

    debt_values = form.data
    value = float(debt_values['value'])
    currency = debt_values['currency']
    debt_values["value"] = CurrencyService.standardize(value, currency)
    debts_service.create_debt(debt_values)
    return redirect(url_for("debts.index"))


@debt_bp.route('/edit/<int:debt_id>', methods=["PUT", "GET"])
@login_required
def edit(debt_id: int):
    debt = Debt.query.get_or_404(debt_id)
    form = DebtForm()
    form_debtor_search = DebtorForm()

    if request.method == 'GET':
        form.process(obj=debt)
        return render_template('debts/edit.html',
            form=form,
            form_search=form_debtor_search
        )

    return str(debt_id);
