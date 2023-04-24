/** autogenerated **/
/**
 *
 **/
 Ext._define('transparency.people_management.trainees.PMLoadDataWindow', {
    extend: 'core.RestfulWindow',

    rest: 'transparency.people_management.trainees.Restful',

    getFormPanel: function() {
        if(!this._formPanel)
            this._formPanel = Ext._create('Ext.form.FormPanel', {
                border: false,
                frame: true,
                width: 500,
                autoHeight: true,
                items: [
                    this.getMonth(),
                    this.getYear()
                ]
            });

        return this._formPanel;
    },

    getMonth: function() {
        if(!this._monthField) {
            this._monthField = new Ext.form.ComboBox({
                fieldLabel: 'Mês do exercício',
                hiddenName: 'mes',
                width: 175,
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
                hiddenName: 'ano',
                width: 175,
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

    getButtons: function() {
        if(!this._buttons)
            this._buttons = [
                {
                    text: 'Fechar',
                    scope: this,
                    handler: function() {
                        this.close();
                    }
                },
                {
                    text: 'Gravar',
                    scope: this,
                    handler: function() {
                        Ext.Msg.show({
                            title: 'Gravando dados',
                            msg: 'Os dados existentes no Portal da Transparência serão atualizados. Deseja continuar?',
                            icon: Ext.Msg.QUESTION,
                            buttons: Ext.Msg.YESNO,
                            scope: this,
                            fn: function(btn) {
                                if (btn === 'no') return;
                
                                this._toSave();
                            }
                        });
                    }
                },
        ];

        return this._buttons;
    },

    _toSave: function() {
        var rest = Ext._create('transparency.people_management.trainees.Restful');
        var mask = new Ext.LoadMask(this.getEl(), { msg: 'Gravando dados...' });

        mask.show();
        rest.generateFromSolicitations(
            this.getFormPanel().getForm().getValues(),
            {
                scope: this,
                fn: function(rst) {
                    Ext.Msg.show({
                        title: 'Gravando dados',
                        msg: 'Os dados foram gravados com sucesso.',
                        icon: Ext.Msg.INFO,
                        scope: this,
                    });
                }
            },
            {
                fn: function() {
                    Ext.Msg.show({
                        title: 'Gravando dados',
                        msg: 'Erro ao gravar os dados.',
                        icon: Ext.Msg.ERROR,
                        buttons: Ext.Msg.OK
                    });
                }
            },
            {
                fn: function() {
                    mask.hide();
                }
            }
        );
    },


    constructor: function(cfg) {
        cfg = core.nullValue(cfg, {});

        Ext.applyIf(cfg, {
            title: 'Carregar Dados no Portal da Transparência',
        });

        Ext.apply(cfg, {
            items: this.getFormPanel(),
        });

        transparency.people_management.trainees.PMLoadDataWindow.superclass.constructor.call(this, cfg);
    },
});

