/** autogenerated **/
/**
 *
 **/
 Ext._define('transparency.people_management.assigned_employees.Grid', {
    extend: 'core.RestfulGrid',

    restWindow: 'transparency.people_management.assigned_employees.Window',
    rest: 'transparency.people_management.assigned_employees.Restful',
    

    configOrderToolBar: ['add', '-', 'loadData', '-', 'search', '->', 'filter', 'download'],

    hideActions: ['remove', 'edit'],

    getColumnModel: function() {
        if(!this._columnModel)
            this._columnModel = Ext._create(
                'Ext.grid.ColumnModel',
                [
                    Ext._create('Ext.grid.RowNumberer'),
                    {header: 'Cod', dataIndex: 'pk', width: 50, hidden: true},
                    {header: 'Tipo', dataIndex: 'from_mp', width: 90, renderer: function(value) { return (value ? 'CEDIDO PELO MP' : 'CEDIDO PARA O MP'); }},
                    {header: 'Mês', dataIndex: 'month', width: 90},
                    {header: 'Ano', dataIndex: 'year', width: 90},
                    {header: 'Matrícula', dataIndex: 'registration', width: 90},
                    {header: 'Nome', dataIndex: 'name', width: 90, id: 'autoExpandColumn'},
                    {header: 'Cargo de Origem', dataIndex: 'original_role', width: 90},
                    {header: 'Cargo Atual', dataIndex: 'current_role', width: 90},
                    {header: 'Função', dataIndex: 'comission_role', width: 90},
                    {header: 'Lotação', dataIndex: 'workplace', width: 90},
                    {header: 'Ato/Portaria nº', dataIndex: 'ordinance_number_assignment', width: 90, renderer: function(value, element, record) {return record.data['ordinance_number_assignment']+'/'+record.data['ordinance_year_assignment']}},
                    {header: 'Data da publicação', dataIndex: 'publication_date_assignment', width: 90},
                    {header: 'Órgão de Origem', dataIndex: 'original_organ', width: 90},
                    {header: 'Órgão de Destino', dataIndex: 'target_organ', width: 90},
                    {header: 'Ônus', dataIndex: 'onus_mp', width: 90, renderer: function(value) { return (value ? 'SIM' : 'NÃO'); }},
                    {header: 'Prazo', dataIndex: 'deadline', width: 90},
                    {header: 'created by', dataIndex: 'created_by_unicode', width: 120, hidden: true},
                    {header: 'modified by', dataIndex: 'modified_by_unicode', width: 120, hidden: true},
                    {header: 'created at', dataIndex: 'created_at', width: 90, renderer: Ext.util.Format.dateRenderer('d/m/Y H:i'), hidden: true},
                    {header: 'modified at', dataIndex: 'modified_at', width: 90, renderer: Ext.util.Format.dateRenderer('d/m/Y H:i'), hidden: true},
                ]
            );

        return this._columnModel;
    },

loadingData: function() {    
    var _window = Ext._create(
        'transparency.people_management.assigned_employees.PMLoadDataWindow'
    );

    _window.show();
},

getLoadDataAction: function () {
    if (!this._loadData)  {
        this._loadData = Ext._create('Ext.Button', {
            text: 'Carregar Dados',
            iconCls: 'icon-agree icon-agree-appointment-new',
            scope: this,
            handler: function () {
                this.loadingData();
            }
        });
    }
    return this._loadData;
},

getFilterAction: function() {
    if(!this._filterAction)
        this._filterAction = Ext._create('Ext.Button', {
            text: 'Filtro',
            iconCls: 'icon-patrimonio icon-pat-filter',
            menu: [
                {
                    text: 'Somente os cedidos pelo MP',
                    checked: false,
                    scope: this,
                    hideOnClick: false,
                    listeners: {
                        scope: this,
                        checkchange: function (item, checked) {
                            if (checked)
                                this.addFilterProperty('from_mp', 'on', 109);
                            else
                                this.removeFilterProperty('from_mp', 109);
                        }
                    }
                },
                {
                    text: 'Somente os cedidos para o MP',
                    checked: false,
                    scope: this,
                    hideOnClick: false,
                    listeners: {
                        scope: this,
                        checkchange: function (item, checked) {
                            if (checked)
                                this.addFilterProperty('from_mp', 'off', 109);
                            else
                                this.removeFilterProperty('from_mp', 109);
                        }
                    }
                },
            ]
        });

    return this._filterAction;
},

});

core.RestfulGrid.register(
    'transparency.people_management.assigned_employees.Restful',
    'transparency.people_management.assigned_employees.Grid'
);


