/** autogenerated **/
/**
 *
 **/
Ext._define('transparency.people_management.employees_members.Restful', {
    extend: 'core.Restful',

    resource: 'TPMEmployeesCache',

    
    generateFromSolicitations: function(values, successCallback, failureCallback, commonCallback) {

        this.doRequest(
            this.getRoute(
                'generate_from_solicitations',
                false,
                'POST',
                {
                    params: values,
                    success: function(xhr) {
                        var rst = Ext.decode(xhr.responseText);

                        if(rst.success) {
                            core.invokeCallback(
                                successCallback || { fn: Ext.emptyFn },
                                rst
                            );
                        } else {
                            core.invokeCallback(
                                failureCallback || { fn: Ext.emptyFn },
                                rst.message
                            );
                        }
                    },
                    failure: function(xhr) {
                        core.invokeCallback(
                            failureCallback || { fn: Ext.emptyFn }
                        );
                    },
                    callback: function(xhr) {
                        core.invokeCallback(commonCallback || { fn: Ext.emptyFn });
                    }
                }
            )
        );
    },

    getFields: function(cfg) {
        if(!this._fields)
            this._fields = transparency.people_management.employees_members.Restful.superclass.getFields.call(this, cfg).concat([
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
                    name: "is_member",
                    type: "bool"
                },
                {
                    name: "is_active",
                    type: "bool"
                },
                {
                    name: "month",
                    type: "int"
                },
                {
                    name: "year",
                    type: "int"
                },
                {
                    name: "registration",
                    type: "string"
                },
                {
                    name: "name",
                    type: "string"
                },
                {
                    name: "effective_role",
                    type: "string"
                },
                {
                    name: "comission_role",
                    type: "string"
                },
                {
                    name: "ordinance_number_nomination",
                    type: "string"
                },
                {
                    name: "ordinance_year_nomination",
                    type: "string"
                },
                {
                    name: "publication_date_nomination",
                    type: "string",
                },
                {
                    name: "ordinance_number_retirement",
                    type: "string"
                },
                {
                    name: "ordinance_retirement",
                    type: "string"
                },
                {
                    name: "ordinance_year_retirement",
                    type: "string"
                },
                {
                    name: "publication_date_retirement",
                    type: "string",
                },
                {
                    name: "workplace",
                    type: "string"
                },
                {
                    name: "stability",
                    type: "bool"
                }
            ]);

        return this._fields;
    }
});