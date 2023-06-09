/** autogenerated **/
/**
 *
 **/
Ext._define('library.CarreiraEstrutura.Restful', {
    extend: 'core.Restful',

    resource: 'MPECarreiraEstrutura',

    getFields: function(cfg) {
        if(!this._fields)
            this._fields = library.CarreiraEstrutura.Restful.superclass.getFields.call(this, cfg).concat([
                {
                    name: "created_by",
                    type: "int",
                    useNull: true
                },
                {
                    name: "created_by_unicode",
                    type: "string"
                },
                {
                    name: "modified_by",
                    type: "int",
                    useNull: true
                },
                {
                    name: "modified_by_unicode",
                    type: "string"
                },
                {
                    name: "created_at",
                    type: "date",
                    dateFormat: "d/m/Y H:i"
                },
                {
                    name: "modified_at",
                    type: "date",
                    dateFormat: "d/m/Y H:i"
                },
                {
                    name: "documento",
                    type: "string"
                }
            ]);

        return this._fields;
    }
});
