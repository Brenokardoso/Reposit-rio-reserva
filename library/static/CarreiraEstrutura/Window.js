/** autogenerated **/
/**
 *
 **/
Ext._define('library.CarreiraEstrutura.Window', {
    extend: 'core.RestfulWindow',

    rest: 'library.CarreiraEstrutura.Restful',

    getFormPanel: function(cfg) {
        if(!this._formPanel)
            this._formPanel = Ext._create('Ext.form.FormPanel', {
                border: false,
                frame: true,
                items: [
                {
                    name: "created_by",
                    fieldLabel: "created by",
                    xtype: "rest-autocompletefield",
                    allowBlank: true,
                    rest: "auth.user.Restful"//
                },
                {
                    name: "modified_by",
                    fieldLabel: "modified by",
                    xtype: "rest-autocompletefield",
                    allowBlank: true,
                    rest: "auth.user.Restful"//
                },
                {
                    name: "created_at",
                    fieldLabel: "created at",
                    xtype: "tk-datetimefield",
                    allowBlank: true
                },
                {
                    name: "modified_at",
                    fieldLabel: "modified at",
                    xtype: "tk-datetimefield",
                    allowBlank: true
                },
                {
                    name: "documento",
                    fieldLabel: "documento",
                    xtype: "textfield",
                    allowBlank: false
                }
            ]
            });

        return this._formPanel;
    }
});

