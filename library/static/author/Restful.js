/** autogenerated **/
/**
 *
 **/
Ext._define('library.author.Restful', {
    extend: 'core.Restful',

    resource: 'BRNAuthor',

    getFields: function(cfg) {
        if(!this._fields)
            this._fields = library.author.Restful.superclass.getFields.call(this, cfg).concat([
                {
                    name: "name",
                    type: "string"
                }
            ]);

        return this._fields;
    }
});
