import ckan.plugins as plugins


class EtalabThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        # Tell CKAN what custom template helper functions this plugin provides,
        # see the ITemplateHelpers plugin interface.
        return dict(
            smart_viewers = smart_viewers,
            )

    def update_config(self, config):
        # Update CKAN's config settings, see the IConfigurer plugin interface.
        plugins.toolkit.add_public_directory(config, 'public')
        plugins.toolkit.add_template_directory(config, 'templates')


def smart_viewers(package):
    """Helper function to extract smart viewers from the related of a package."""
    return [
        related
        for related in package.related
        if related.type == 'smart_viewer'
        ]
