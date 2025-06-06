import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OauthScope(str, enum.Enum):
    AUTHORIZED_USER_READ = "authorized_user:read"
    """
    read details about the authorized user
    """

    ASSETS_READ = "assets:read"
    """
    read assets on the site
    """

    ASSETS_WRITE = "assets:write"
    """
    write assets on a site
    """

    CMS_READ = "cms:read"
    """
    read collections and items for a site
    """

    CMS_WRITE = "cms:write"
    """
    write to collections and items for a site
    """

    CUSTOM_CODE_READ = "custom_code:read"
    """
    read custom code on the site
    """

    CUSTOM_CODE_WRITE = "custom_code:write"
    """
    modify custom code on the site
    """

    ECOMMERCE_READ = "ecommerce:read"
    """
    read ecommerce data
    """

    ECOMMERCE_WRITE = "ecommerce:write"
    """
    edit ecommerce data
    """

    FORMS_READ = "forms:read"
    """
    read form data
    """

    FORMS_WRITE = "forms:write"
    """
    write form data
    """

    PAGES_READ = "pages:read"
    """
    read pages on the site
    """

    PAGES_WRITE = "pages:write"
    """
    write to pages on the site
    """

    SITES_READ = "sites:read"
    """
    read sites on the site
    """

    SITES_WRITE = "sites:write"
    """
    modify pages on the site
    """

    USERS_READ = "users:read"
    """
    read users on the site
    """

    SITE_ACTIVITY_READ = "site_activity:read"
    """
    read site activity logs
    """

    USERS_WRITE = "users:write"
    """
    modify users on the site
    """

    WORKSPACE_READ = "workspace:read"
    """
    read workspace resource data
    """

    WORKSPACE_WRITE = "workspace:write"
    """
    write workspace resource data
    """

    SITE_CONFIG_READ= "site_config:read"
    """
    read site configuration data
    """

    SITE_CONFIG_WRITE= "site_config:write"
    """
    write site configuration data
    """

    def visit(
        self,
        authorized_user_read: typing.Callable[[], T_Result],
        assets_read: typing.Callable[[], T_Result],
        assets_write: typing.Callable[[], T_Result],
        cms_read: typing.Callable[[], T_Result],
        cms_write: typing.Callable[[], T_Result],
        custom_code_read: typing.Callable[[], T_Result],
        custom_code_write: typing.Callable[[], T_Result],
        ecommerce_read: typing.Callable[[], T_Result],
        ecommerce_write: typing.Callable[[], T_Result],
        forms_read: typing.Callable[[], T_Result],
        forms_write: typing.Callable[[], T_Result],
        pages_read: typing.Callable[[], T_Result],
        pages_write: typing.Callable[[], T_Result],
        sites_read: typing.Callable[[], T_Result],
        sites_write: typing.Callable[[], T_Result],
        users_read: typing.Callable[[], T_Result],
        site_activity_read: typing.Callable[[], T_Result],
        users_write: typing.Callable[[], T_Result],
        workspace_read: typing.Callable[[], T_Result],
        workspace_write: typing.Callable[[], T_Result],
        site_config_read: typing.Callable[[], T_Result],
        site_config_write: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.AUTHORIZED_USER_READ:
            return authorized_user_read()
        if self is OauthScope.ASSETS_READ:
            return assets_read()
        if self is OauthScope.ASSETS_WRITE:
            return assets_write()
        if self is OauthScope.CMS_READ:
            return cms_read()
        if self is OauthScope.CMS_WRITE:
            return cms_write()
        if self is OauthScope.CUSTOM_CODE_READ:
            return custom_code_read()
        if self is OauthScope.CUSTOM_CODE_WRITE:
            return custom_code_write()
        if self is OauthScope.ECOMMERCE_READ:
            return ecommerce_read()
        if self is OauthScope.ECOMMERCE_WRITE:
            return ecommerce_write()
        if self is OauthScope.FORMS_READ:
            return forms_read()
        if self is OauthScope.FORMS_WRITE:
            return forms_write()
        if self is OauthScope.PAGES_READ:
            return pages_read()
        if self is OauthScope.PAGES_WRITE:
            return pages_write()
        if self is OauthScope.SITES_READ:
            return sites_read()
        if self is OauthScope.SITES_WRITE:
            return sites_write()
        if self is OauthScope.USERS_READ:
            return users_read()
        if self is OauthScope.SITE_ACTIVITY_READ:
            return site_activity_read()
        if self is OauthScope.USERS_WRITE:
            return users_write()
        if self is OauthScope.WORKSPACE_READ:
            return workspace_read()
        if self is OauthScope.WORKSPACE_WRITE:
            return workspace_write()
        if self is OauthScope.SITE_CONFIG_READ:
            return site_config_read()
        if self is OauthScope.SITE_CONFIG_WRITE:
            return site_config_write()