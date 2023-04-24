/** autogenerated **/
/**
 *
 **/
Ext._define('transparency.people_management.employees_members.Window', {
	extend: 'core.RestfulWindow',

	rest: 'transparency.people_management.employees_members.Restful',

	getFormPanel: function () {
		if (!this._formPanel)
			this._formPanel = Ext._create('Ext.form.FormPanel', {
				border: false,
				frame: true,
				width: 650,
				autoHeight: true,
				items: [
					this.getMonth(),
					this.getYear(),
					{
						name: "registration",
						fieldLabel: "Matr\u00edcula",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 50,
						width: 200
					},
					{
						name: "name",
						fieldLabel: "Nome",
						xtype: "textfield",
						allowBlank: false,
						maxLength: 100,
						width: 200
					},
					{
						name: "effective_role",
						fieldLabel: "Cargo Efetivo",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 100,
						width: 200
					},
					{
						name: "comission_role",
						fieldLabel: "Função",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 120,
						width: 200
					},
					{
						name: "workplace",
						fieldLabel: "Lotação",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 120,
						width: 200
					},
					{
						name: "ordinance_number_nomination",
						fieldLabel: "N\u00famero do Ato/Portaria (Nomeação)",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 20,
						width: 200
					},
					{
						name: "ordinance_year_nomination",
						fieldLabel: "Ano do Ato/Portaria(Nomeação)",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 4,
						width: 200
					},
					{
						name: "publication_date_nomination",
						fieldLabel: "Data da Publicação (Nomeação)",
						xtype: "datefield",
						allowBlank: true,
						width: 200
					},
					{
						name: "ordinance_number_retirement",
						fieldLabel: "N\u00famero do Ato/Portaria (Aposentadoria)",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 20,
						width: 200
					},
					{
						name: "ordinance_year_retirement",
						fieldLabel: "Ano do Ato/Portaria (Aposentadoria)",
						xtype: "textfield",
						allowBlank: true,
						maxLength: 4,
						width: 200
					},
					{
						name: "publication_date_retirement",
						fieldLabel: "Data da Publicação (Aposentadoria)",
						xtype: "datefield",
						allowBlank: true,
						width: 200
					},
					{
						name: "stability",
						fieldLabel: "",
						xtype: "checkbox",
						allowBlank: false,
						boxLabel: "Estabilidade/Vitaliciedade",
						width: 200
					}
				]
			});

		return this._formPanel;
	},

	getMonth: function() {
        if(!this._monthField) {
            this._monthField = new Ext.form.ComboBox({
                fieldLabel: 'Mês do exercício',
                hiddenName: 'month',
                width: 200,
                store: [
                    [ 1, 'JANEIRO'],
                    [ 2, 'FEVEREIRO'],
                    [ 3, 'MARÇO'],
                    [ 4, 'ABRIL'],
                    [ 5, 'MAIO'],
                    [ 6, 'JUNHO'],
                    [ 7, 'JULHO'],
                    [ 8, 'AGOSTO'],
                    [ 9, 'SETEMBRO'],
                    [10, 'OUTUBRO'],
                    [11, 'NOVEMBRO'],
                    [12, 'DEZEMBRO']
                ],
                allowBlank: false,
                triggerAction: 'all',
                mode: 'local'
            });
        }
        return this._monthField
    },

    getYear: function() {
        if(!this._yearField) {
            this._yearField = new Ext.form.ComboBox({
                fieldLabel: 'Ano do exercício',
                hiddenName: 'year',
                width: 200,
                store: [
                    [ 2023, '2023'],
                    [ 2022, '2022'],
                    [ 2021, '2021'],
                    [ 2020, '2020'],
                    [ 2019, '2019'],
                    [ 2018, '2018'],
                    [ 2017, '2017'],
                    [ 2016, '2016'],
                    [ 2015, '2015']
                ],
                allowBlank: false,
                triggerAction: 'all',
                mode: 'local'
            });
        }
        return this._yearField
    },
});

