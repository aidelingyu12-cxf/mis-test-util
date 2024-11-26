# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppTesters(models.Model):
    tester_name = models.CharField(max_length=64)
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_testers'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CMembership(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    login_id = models.CharField(max_length=32, blank=True, null=True)
    memship_no = models.CharField(max_length=45, blank=True, null=True)
    level_id = models.CharField(max_length=32, blank=True, null=True)
    photo_url = models.CharField(max_length=500, blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    member_name = models.CharField(max_length=45, blank=True, null=True)
    member_spell_name = models.CharField(max_length=100, blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    male = models.CharField(max_length=1, blank=True, null=True)
    del_flag = models.CharField(max_length=1, blank=True, null=True)
    cell_phone = models.CharField(unique=True, max_length=45, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    create_user = models.CharField(max_length=32, blank=True, null=True)
    update_user = models.CharField(max_length=32, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    openid = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    operator_id = models.CharField(max_length=32, blank=True, null=True)
    operator_bind_status = models.CharField(max_length=1, blank=True, null=True)
    survey_status = models.CharField(max_length=1, blank=True, null=True)
    vip_value = models.CharField(max_length=16, blank=True, null=True)
    nick_name = models.CharField(max_length=64, blank=True, null=True)
    date_of_birth = models.CharField(max_length=10, blank=True, null=True)
    maker_id = models.CharField(max_length=32, blank=True, null=True)
    watch_guide_video_status = models.CharField(max_length=1)
    notify_push_status = models.CharField(max_length=1)
    first_login_datetime = models.DateTimeField(blank=True, null=True)
    first_time_mis_device_id = models.CharField(max_length=120, blank=True, null=True)
    first_time_mis_device_date_time = models.DateTimeField(blank=True, null=True)
    has_unread_check_report = models.CharField(max_length=1)
    latest_succeed_task_id = models.CharField(max_length=32, blank=True, null=True)
    has_paid_order = models.CharField(max_length=1, blank=True, null=True)
    maker_bound_indicator = models.CharField(max_length=1)
    maker_bound_datetime = models.DateTimeField(blank=True, null=True)
    maker_bound_channel = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_membership'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Maker(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    health_certificate = models.CharField(max_length=255, blank=True, null=True)
    id_photos = models.TextField(blank=True, null=True)
    bank_card_number = models.CharField(max_length=255, blank=True, null=True)
    opening_bank = models.CharField(max_length=255, blank=True, null=True)
    recommend_code = models.CharField(max_length=255, blank=True, null=True)
    del_flag = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    account_id = models.CharField(max_length=255, blank=True, null=True)
    audit_flag = models.CharField(max_length=10, blank=True, null=True)
    first_trial_user_id = models.CharField(max_length=64, blank=True, null=True)
    retrial_user_id = models.CharField(max_length=64, blank=True, null=True)
    opened_indicator = models.CharField(max_length=10, blank=True, null=True)
    opened_date = models.CharField(max_length=64, blank=True, null=True)
    anxinsign_user_id = models.CharField(max_length=64, blank=True, null=True)
    contract_nbr = models.CharField(max_length=64, blank=True, null=True)
    contract_state = models.CharField(max_length=10, blank=True, null=True)
    expired_date = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)
    reject_reason = models.CharField(max_length=255, blank=True, null=True)
    default_flag = models.CharField(max_length=10, blank=True, null=True)
    id_number = models.CharField(max_length=64, blank=True, null=True)
    provincial_agent_id = models.CharField(max_length=64, blank=True, null=True)
    location_city_id = models.CharField(max_length=10, blank=True, null=True)
    location_district_id = models.CharField(max_length=10, blank=True, null=True)
    location_province_id = models.CharField(max_length=10, blank=True, null=True)
    nick_name = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.CharField(max_length=64, blank=True, null=True)
    contract_create_time = models.CharField(max_length=64, blank=True, null=True)
    contract = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    xye_flag = models.CharField(max_length=10, blank=True, null=True)
    xye_reject_reason = models.CharField(max_length=255, blank=True, null=True)
    id_address = models.CharField(max_length=255, blank=True, null=True)
    cert_date = models.CharField(max_length=64, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker'


class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
