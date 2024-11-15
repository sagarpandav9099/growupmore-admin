$(document).ready(function () {
    // Kendo Grid Initialization
    $("#countryGrid").kendoGrid({
        dataSource: {
            transport: {
                read: {
                    url: "/countries/",
                    dataType: "json"
                }
            },
            pageSize: 10
        },
        pageable: true,
        sortable: true,
        filterable: true,
        columns: [
            { field: "name", title: "Name" },
            { field: "iso3", title: "ISO3" },
            { field: "phone_code", title: "Phone Code" },
            { field: "status", title: "Status" },
            {
                field: "actions",
                title: "Actions",
                template: function (dataItem) {
                    return `
                        <button class="btn btn-warning edit-country" data-id="${dataItem.id}">Edit</button>
                        <button class="btn btn-danger delete-country" data-id="${dataItem.id}">Delete</button>`;
                }
            }
        ]
    });

    // Create Country Handler
    $("#createCountryForm").submit(function (e) {
        e.preventDefault();
        const formData = new FormData(this);

        $.ajax({
            type: "POST",
            url: "/countries/new/",
            data: formData,
            processData: false,
            contentType: false,
            success: function () {
                $("#countryGrid").data("kendoGrid").dataSource.read();
                alert("Country added successfully!");
            },
            error: function () {
                alert("Failed to add country.");
            }
        });
    });

    // Delete Country Handler
    $(document).on("click", ".delete-country", function () {
        const countryId = $(this).data("id");
        $.ajax({
            type: "POST",
            url: `/countries/delete/${countryId}/`,
            success: function () {
                $("#countryGrid").data("kendoGrid").dataSource.read();
                alert("Country deleted successfully!");
            },
            error: function () {
                alert("Failed to delete country.");
            }
        });
    });
});
