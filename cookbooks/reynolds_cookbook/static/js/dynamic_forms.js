// static/js/dynamic_forms.js

document.addEventListener('DOMContentLoaded', function () {
    function addForm(formDivId, formPrefix) {
        var formDiv = document.getElementById(formDivId);
        var totalForms = document.getElementById(`id_${formPrefix}-TOTAL_FORMS`);
        var currentFormCount = parseInt(totalForms.value);
        var newForm = formDiv.firstElementChild.cloneNode(true);
        var formRegex = new RegExp(`${formPrefix}-(\\d+)`, 'g');

        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `${formPrefix}-` + currentFormCount);
        formDiv.appendChild(newForm);
        totalForms.value = currentFormCount + 1;
    }

    document.getElementById('add-ingredient').addEventListener('click', function () {
        addForm('ingredient-forms', 'ingredient_set');
    });

    document.getElementById('add-instruction').addEventListener('click', function () {
        addForm('instruction-forms', 'instruction_set');
    });
});
