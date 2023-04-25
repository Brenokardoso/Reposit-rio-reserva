/** autogenerated **/
/**
 *
 **/
Ext._define('library.CarreiraEstrutura.Grid', {
    extend: 'core.RestfulGrid',

    restWindow: 'library.CarreiraEstrutura.Window',

    getColumnModel: function() {
        if(!this._columnModel)
            this._columnModel = Ext._create(
                'Ext.grid.ColumnModel',
                [
                    Ext._create('Ext.grid.RowNumberer'),
                    {header: 'Cod', dataIndex: 'pk', width: 50, hidden: true},
                    {header: 'Descricao', dataIndex: 'unicode', id: 'autoExpandColumn'},
                    {header: 'created by', dataIndex: 'created_by_unicode', width: 120},
                    {header: 'modified by', dataIndex: 'modified_by_unicode', width: 120},
                    {header: 'created at', dataIndex: 'created_at', width: 90, renderer: Ext.util.Format.dateRenderer('d/m/Y H:i')},
                    {header: 'modified at', dataIndex: 'modified_at', width: 90, renderer: Ext.util.Format.dateRenderer('d/m/Y H:i')},
                    {header: 'documento', dataIndex: 'documento', width: 90}
                ]
            );

        return this._columnModel;
    }
});

core.RestfulGrid.register(
    'library.CarreiraEstrutura.Restful',
    'library.CarreiraEstrutura.Grid'
);

