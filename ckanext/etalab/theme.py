import ckan.plugins as plugins

# Our custom template helper function.
def example_helper():
    '''An example template helper function.'''

    # Just return some example text.
    return 'This is some example text.'

class EtalabThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        # Tell CKAN what custom template helper functions this plugin provides,
        # see the ITemplateHelpers plugin interface.
        return {'example_helper': example_helper}

    def update_config(self, config):
        # Update CKAN's config settings, see the IConfigurer plugin interface.
        plugins.toolkit.add_public_directory(config, 'public')
        plugins.toolkit.add_template_directory(config, 'templates')
