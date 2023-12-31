# Generated by Django 4.1.7 on 2023-04-24 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(db_column='cart_ID', primary_key=True, serialize=False)),
                ('cart_amount', models.FloatField(blank=True, null=True)),
                ('cart_noitems', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(db_column='category_ID', primary_key=True, serialize=False)),
                ('category_type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('date_of_creation', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='DatabaseAdministrator',
            fields=[
                ('administrator_id', models.IntegerField(db_column='administrator_ID', primary_key=True, serialize=False)),
                ('admin_first_name', models.CharField(max_length=255)),
                ('admin_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_phone_number', models.IntegerField()),
                ('position_of_responsiblity', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'database_administrator',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(db_column='order_ID', primary_key=True, serialize=False)),
                ('order_placed_on', models.DateTimeField(blank=True, null=True)),
                ('payable_amount', models.FloatField()),
                ('stats', models.CharField(max_length=255)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.cart')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('phone_number', models.IntegerField(primary_key=True, serialize=False)),
                ('location_pincode', models.IntegerField()),
            ],
            options={
                'db_table': 'phone_number',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(db_column='product_ID', primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('product_reviews', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_id', models.IntegerField(db_column='seller_ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('bank_ifsc_code', models.IntegerField(db_column='bank_IFSC_code')),
                ('bank_name', models.CharField(max_length=255)),
                ('branch_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
        migrations.CreateModel(
            name='TrackingAndCancellation',
            fields=[
                ('tracking_id', models.IntegerField(db_column='tracking_ID', primary_key=True, serialize=False)),
                ('delivery_status', models.CharField(max_length=10)),
                ('cancellation_status', models.CharField(blank=True, max_length=10, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.orders')),
            ],
            options={
                'db_table': 'tracking_and_cancellation',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('shipping_id', models.IntegerField(db_column='shipping_ID', primary_key=True, serialize=False)),
                ('reciever_name', models.CharField(blank=True, max_length=255, null=True)),
                ('receiver_phonenumber', models.IntegerField(blank=True, db_column='receiver_phoneNumber', null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.customer')),
            ],
            options={
                'db_table': 'shipping_address',
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('stock_id', models.IntegerField(db_column='stock_ID', primary_key=True, serialize=False)),
                ('stock_left', models.IntegerField(blank=True, null=True)),
                ('total_stock', models.IntegerField(blank=True, null=True)),
                ('pro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.product')),
            ],
            options={
                'db_table': 'product_stock',
            },
        ),
        migrations.CreateModel(
            name='ProductDescriptors',
            fields=[
                ('descriptor_id', models.IntegerField(db_column='descriptor_ID', primary_key=True, serialize=False)),
                ('file_caption', models.CharField(blank=True, max_length=255, null=True)),
                ('pro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.product')),
            ],
            options={
                'db_table': 'product_descriptors',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('transaction_id', models.IntegerField(db_column='transaction_ID', primary_key=True, serialize=False)),
                ('mode_of_payment', models.CharField(max_length=255)),
                ('delivery_charges', models.FloatField(blank=True, null=True)),
                ('status_of_transaction', models.CharField(max_length=255)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.orders')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='shipp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.shippingaddress'),
        ),
        migrations.CreateModel(
            name='InCartProducts',
            fields=[
                ('incart_id', models.IntegerField(db_column='incart_ID', primary_key=True, serialize=False)),
                ('quantity_of_products', models.IntegerField()),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.cart')),
                ('pro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.product')),
            ],
            options={
                'db_table': 'in_cart_products',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='cust',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shopstop.customer'),
        ),
    ]
