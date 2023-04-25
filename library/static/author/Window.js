/** autogenerated **/
/**
 *
 **/
Ext._define('library.author.Window', {
    extend: 'core.RestfulWindow',

    rest: 'library.author.Restful',

    getFormPanel: function(cfg) {
        if(!this._formPanel)
            this._formPanel = Ext._create('Ext.form.FormPanel', {
                border: false,
                frame: true,
                items: [
                {
                    name: "name",
                    fieldLabel: "name",
                    xtype: "textfield",
                    allowBlank: false,
                    maxLength: 200
                }
            ]
            });

        return this._formPanel;
    }
});

