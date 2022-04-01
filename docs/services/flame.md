# Flame

[Flame](https://github.com/pawelmalak/flame) is an application dashboard and startpage for the home server. It can be configured to host link to apps in docker/kubernetes, and also bookmarks for various sites. For this deployment, only docker is supported, deployed apps on the same host will be automatically added.

**Note**: Since Flame is an app that changes regularly, this implementation was tested with version `v2.3.0`. If issues are encountered with later versions, fix the version to the tested version and please open an issue to address and fix.

## Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| flame_version | no | `latest` | Flame version - available version can be found [here](https://github.com/pawelmalak/flame/releases). Defaults to `latest` - note: if API issues are encountered check above what version was tested, and set this to that version |
| flame_network | no | `core` | Network that flame will attach itself to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| flame_password | yes | `p@ssw0rd` | Password for the admin user for Flame
| flame_autoupdate | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for Flame, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |
| flame_config | no | [Flame Config](#flame-config) | The Flame app configuration |
| flame_apps | no | List of [Flame Apps](#apps) | List of additional flame apps to add to the dashboard |

## Flame Config

| Config | Default | Description |
|--------|---------|-------------|
| apps_same_tab | `false` | Whether to open apps in the same tab, or a new tab |
| bookmarks_same_tab | `false` | Whether to open bookmarks in the same tab, or a new tab |
| custom_title | `Flame` | Custom webpage title |
| day_schema | `"Sunday;Monday;Tuesday;Wednesday;Thursday;Friday;Saturday"` | Names for the days shown in the header |
| default_search_provider | `"l"` | The search provider to use. To find the right value here, check the [supported queries](https://github.com/pawelmalak/flame/blob/7eb8ec228ab789412265fd72f8e71555c2895c71/client/src/utility/searchQueries.json) - For some examples, `l` is Local Search, `d` is DuckDuckGo, `g` is Google |
| default_theme | `blackboard` | The default theme to use, a list of themese can be found [here](https://github.com/pawelmalak/flame/blob/fd7d8e65c8238a9f31e10721651728c33cea2a88/client/src/components/Settings/Themer/themes.json) |
| disable_autofocus | `false` | Disables auto focus on the search bar |
| docker_apps | `true` | Whether to enable docker integration |
| docker_host | `localhost` | Docker host to use. If docker is remote, follow [these instructions](https://github.com/pawelmalak/flame#docker-integration) to connect |
| greeting_schema | `"Good evening!;Good afternoon!;Good morning!;Good night!"` | Greetings for the header. These have to be 4 values, separated by `;`
| hide_apps | `false` | Whether to hide the Apps section in the UI |
| hide_categories | `false` | Whether to hide the Categories section in the UI |
| hide_date | `false` | Whether to hide the Date in the UI |
| hide_header | `false` | Whether to hide the Header section in the UI |
| hide_search | `false` | Whether to hide the Search section in the UI |
| is_celsius | `true` | Whether to use C or F for temperature display |
| is_kilometer | `true` | Whether to use Km or miles for distance display |
| lat | `0` | Latitude for the location for which to display the weather info - more info [here](https://github.com/pawelmalak/flame#setting-up-weather-module) |
| long | `0` | Longitude for the location for which to display the weather info - more info [here](https://github.com/pawelmalak/flame#setting-up-weather-module) |
| month_schema | `"January;February;March;April;May;June;July;August;September;October;November;December"` | Month names to use when displaying in the header |
| pin_apps_by_default | `true` | Whether to pin apps by default |
| pin_categories_by_default | `true` | Whether to pin categories by default |
| search_same_tab | `false` | Whether to open search in the same or new tab |
| show_time | `false` | Whether to show time in the UI |
| unpin_stopped_apps | `false` | Whether to unpin stopped docker/k8s apps |
| use_american_date | `false` | Whether to use month-day-year or day-month-year to display dates |
| use_ordering | `name` | What type of ordering to use for apps. Options are `name` (alphabetical order), `createdAt` (creation order) and `custom` (custom order can be set through the UI) |
| weather_data | `cloud` | Whether to should cloud coverage (`cloud`) or humidity (`humidity`) as additional data for the weather |
| weather_api_key | `""` | [Weather API](https://www.weatherapi.com/pricing.aspx) key - this is free for up to 1M requests per month, Flame averages about 3K calls per month |

## Apps

You can define a set of additional apps to be shown in Flame. Apps on the same host as the Flame instance will automatically be added if `docker_apps` configuration is set to `true`.
Configuration for the apps is as follows:

| Config | Example | Description |
|--------|---------|-------------|
| name | `Example` | Under what name the app should be displayed |
| url | `example.domain.local` | The host/URL for the app |
| icon | `app` | The name of the [Material Design Icon](https://materialdesignicons.com/) to be set for the application. |

## Bookmarks

Bookmarks are not supported for automatic configuration.
