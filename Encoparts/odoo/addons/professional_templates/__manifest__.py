# -*- coding: utf-8 -*-
{
    'name': "Professional Report Templates",

    'summary': """
        Professional Report Templates: Purchase Order, RFQ, Sales Order, Quotation, Invoice, Delivery Note and Picking List""",

    'description': """
    Below are some of the main features (Full documentation coming soon):

    Covers Purchase Order, RFQ, Sales Order, Quotation, Delivery Note and Picking List

    5 different Report Templates to choose from for each report type mentioned above

    Upload high resolution company logo for each report

    Set the theme colors for your report to match your company colors

    You can set the text color for Company name in the report sesparately

    You can set the text color for Customer name in the report separately

    You can set the Background Color for odd and even lines (i.e quotation lines, order lines) in all the reports

    Line numbering for all lines (i.e quotation lines, order lines)

    You will be able to configure default  colors and theme settings for all reports (found in the company form) and also custom settings per report generated

    We can also do more customizations upon purchase (at minimal or no cost at all) depending on the feature you want
    """,

    'author': "Optima ICT Services LTD",
    'website': "http://www.optima.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting & Finance',
    'images': ['static/description/main.png'],

    'version': '1.0',
    'price': 129,
    'currency': 'EUR',
    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'purchase', 'stock', 'delivery'],
   # 'external_dependencies': {'python': ['num2words']},

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/res_company_view.xml',
        'views/res_currency.xml',
        'views/res_partner.xml',
        'views/company_footer.xml',
        'views/company_address.xml',
        'views/category.xml',
        'views/report_style_views.xml',

        'reports/invoice_reports.xml',
        'reports/sale_order_reports.xml',
        'reports/purchase_order_reports.xml',
        'reports/rfq_reports.xml',
        'reports/delivery_reports.xml',
        'reports/stock_picking_report.xml',

        'invoice/invoice_lines.xml',
        'invoice/switch_templates.xml',
        'invoice/dl_envelope.xml',
        'invoice/modern_template.xml',
        'invoice/classic_template.xml',
        'invoice/retro_template.xml',
        'invoice/tva_template.xml',
        'invoice/odoo_template.xml',
        'invoice/account_invoice_view.xml',
        'invoice/invoice_lines_no_layout.xml',

        'sale_order/order_lines.xml',
        'sale_order/switch_templates.xml',
        'sale_order/sale_order_view.xml',
        'sale_order/odoo_template.xml',
        'sale_order/retro_template.xml',
        'sale_order/classic_template.xml',
        'sale_order/tva_template.xml',
        'sale_order/modern_template.xml',

        'purchase_order/purchase_lines.xml',
        'purchase_order/switch_templates.xml',
        'purchase_order/purchase_order_view.xml',
        'purchase_order/odoo_template.xml',
        'purchase_order/retro_template.xml',
        'purchase_order/classic_template.xml',
        'purchase_order/tva_template.xml',
        'purchase_order/modern_template.xml',


        'rfq/rfq_lines.xml',
        'rfq/switch_templates.xml',
        'rfq/rfq_view.xml',
        'rfq/odoo_template.xml',
        'rfq/retro_template.xml',
        'rfq/classic_template.xml',
        'rfq/tva_template.xml',
        'rfq/modern_template.xml',

        'delivery_note/switch_templates.xml',
        'delivery_note/delivery_lines.xml',
        'delivery_note/delivery_note_view.xml',
        'delivery_note/odoo_template.xml',
        'delivery_note/retro_template.xml',
        'delivery_note/classic_template.xml',
        'delivery_note/tva_template.xml',
        'delivery_note/modern_template.xml',

        'picking/switch_templates.xml',
        'picking/picking_lines.xml',
        'picking/picking_view.xml',
        'picking/odoo_template.xml',
        'picking/retro_template.xml',
        'picking/classic_template.xml',
        'picking/tva_template.xml',
        'picking/modern_template.xml',


        'carrier/delivery_report.xml',
        'carrier/picking_report.xml',

        'data/res_currency_data.xml',
        'data/default_style.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
