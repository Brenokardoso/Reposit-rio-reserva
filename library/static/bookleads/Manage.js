/** autogenerated **/
Ext._define('library.bookleads.Manage', {
    extend: 'toolkit.widget.TabPanel',

    getBookLeadGrid: function() {
        if(!this._grid) {
            this._grid = Ext._create('library.bookleads.Grid', {
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
                title: 'BookLead'
            }
        );

        Ext.apply(
            cfg,
            {
                layout: 'border',
                items: [
                    this.getBookLeadGrid(),
                ]
            }
        );

        library.bookleads.Manage.superclass.constructor.call(this, cfg);
    }
});
