/** autogenerated **/
/**
 *
 **/
 Ext._define('transparency.people_management.assigned_employees.Restful', {
    extend: 'core.Restful',

    resource: 'TPMAssignedEmployeesCache',

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
            this._fields = transparency.people_management.assigned_employees.Restful.superclass.getFields.call(this, cfg).concat([
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
                    name: "month",
                    type: "string"
                },
                {
                    name: "year",
                    type: "string"
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
                    name: "original_role",
                    type: "string"
                },
                {
                    name: "current_role",
                    type: "string"
                },
                {
                    name: "comission_role",
                    type: "string"
                },
                {
                    name: "ordinance_year_assignment",
                    type: "string"
                },
                {
                    name: "ordinance_number_assignment",
                    type: "string"
                },
                {
                    name: "publication_date_assignment",
                    type: "string"
                },
                {
                    name: "workplace",
                    type: "string"
                },
                {
                    name: "original_organ",
                    type: "string"
                },
                {
                    name: "target_organ",
                    type: "string"
                },
                {
                    name: "deadline",
                    type: "string"
                },
                {
                    name: "onus_mp",
                    type: "bool"
                },
                {
                    name: "from_mp",
                    type: "bool"
                }
            ]);

        return this._fields;
    }
});
