/** autogenerated **/
/**
 *
 **/
Ext._define('paidcareer.careerandstructure.Window', {
    extend: 'core.RestfulWindow',

    rest: 'paidcareer.careerandstructure.Restful',

    getFormPanel: function(cfg) {
        if(!this._formPanel)
            this._formPanel = Ext._create('Ext.form.FormPanel', {
                border: false,
                frame: true,
                items: [
                {
                    name: "modified_by",
                    fieldLabel: "modified by",
                    xtype: "rest-autocompletefield",
                    allowBlank: true,
                    rest: "auth.userRestful"
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
                    name: "created_by",
                    fieldLabel: "created by",
                    xtype: "rest-autocompletefield",
                    allowBlank: false,
                    rest: "auth.userRestful"
                },
                {
                    name: "updated_by",
                    fieldLabel: "updated by",
                    xtype: "rest-autocompletefield",
                    allowBlank: false,
                    rest: "auth.userRestful"
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

