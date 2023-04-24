/** autogenerated **/
Ext._define('transparency.people_management.remuneration_structure_members.Manage', {
    extend: 'toolkit.widget.TabPanel',

    getGrid: function() {
        if(!this._grid) {
            this._grid = Ext._create('transparency.people_management.remuneration_structure_members.Grid', {
                region: 'center',
                gridAutoLoad: false
            });
        }

        return this._grid;
    },

    constructor: function(cfg) {
        cfg = core.nullValue(cfg, {});

        Ext.applyIf(
            cfg,
            {
                title: 'Estrutura Remuneratória - Membros'
            }
        );

        Ext.apply(
            cfg,
            {
                layout: 'border',
                items: [
                    this.getGrid(),
                ]
            }
        );

        transparency.people_management.remuneration_structure_members.Manage.superclass.constructor.call(this, cfg);
    }
});

