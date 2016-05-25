# Cloud Foundry Node.js Buildpack
[![CF Slack](https://s3.amazonaws.com/buildpacks-assets/buildpacks-slack.svg)](http://slack.cloudfoundry.org)

A Cloud Foundry [buildpack](http://docs.cloudfoundry.org/buildpacks/) for Node based apps.

This is based on the [Heroku buildpack] (https://github.com/heroku/heroku-buildpack-nodejs).

Additional documentation can be found at the [CloudFoundry.org](http://docs.cloudfoundry.org/buildpacks/node/index.html).

## Using the Buildpack

For information on deploying Node.js applications visit [CloudFoundry.org](http://docs.cloudfoundry.org/buildpacks/node/index.html).

## Using the AppDynamics Agent Framework

The AppDynamics Agent Framework causes an application to be automatically configured to work with a bound <a href="http://www.appdynamics.com">AppDynamics Service </a>.

<table>
  <tr>
    <td><strong>Detection Criterion</strong></td><td>Existence of a single bound AppDynamics service. The existence of an AppDynamics service defined by the <a href="http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#VCAP-SERVICES"><code>VCAP_SERVICES</code></a> payload containing a service name with <code>appdynamics</code> as a substring.</td>
  </tr>
</table>

### User-Provided Service
When binding AppDynamics using a user-provided service, it must have name or tag with `appdynamics` in it. The credential payload can contain the following entries:

| Name | Description
| ---- | -----------
| `account-access-key` | The account access key to use when authenticating with the controller
| `account-name` | (Optional) The account name to use when authenticating with the controller
| `application-name` | (Optional) the application's name
| `host-name` | The controller host name
| `node-name` | (Optional) the application's node name
| `port` | The controller port
| `ssl-enabled` | (Optional) Whether or not to use an SSL connection to the controller
| `tier-name` | (Optional) the application's tier name

# Building the Buildpack

1. Make sure you have fetched submodules

  ```bash
  git submodule update --init
  ```

1. Get latest buildpack dependencies

  ```shell
  BUNDLE_GEMFILE=cf.Gemfile bundle
  ```

1. Build the buildpack

  ```shell
  BUNDLE_GEMFILE=cf.Gemfile bundle exec buildpack-packager [ --cached | --uncached ]
  ```

1. Use in Cloud Foundry

  Upload the buildpack to your Cloud Foundry and optionally specify it by name

  ```bash
  cf create-buildpack custom_node_buildpack node_buildpack-offline-custom.zip 1
  cf push my_app -b custom_node_buildpack
  ```

## Testing
Buildpacks use the [Machete](https://github.com/cloudfoundry/machete) framework for running integration tests.

To test a buildpack, run the following command from the buildpack's directory:

```
BUNDLE_GEMFILE=cf.Gemfile bundle exec buildpack-build
```

More options can be found on Machete's [Github page.](https://github.com/cloudfoundry/machete)

## Contributing

Find our guidelines [here](./CONTRIBUTING.md).

## Help and Support

Join the #buildpacks channel in our [Slack community] (http://slack.cloudfoundry.org/)

## Reporting Issues

Open an issue on this project

## Active Development

The project backlog is on [Pivotal Tracker](https://www.pivotaltracker.com/projects/1042066)
