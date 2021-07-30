![LambdaTest Logo](https://www.lambdatest.com/static/images/logo.svg)
---

# python-behave-sample
Behave integration with LambdaTest<br/>


### Setup
Install depedencies ```pip install -r requirements.txt```
### Configuration steps
##### Setting locally
- Set LambdaTest username and access key in environment variables. It can be obtained from [LambdaTest dashboard](https://automation.lambdatest.com/)
example:
- For linux/mac
```
   export LT_USERNAME="YOUR_USERNAME"
   export LT_ACCESS_KEY="YOUR ACCESS KEY"
  
```
- For Windows
```
   set LT_USERNAME="YOUR_USERNAME"
   set LT_ACCESS_KEY="YOUR ACCESS KEY"
  
```
 For setting capaibilies,Update `config.json`  (List of supported OS platfrom, Browser, resolutions can be found at [LambdaTest capability generator](https://www.lambdatest.com/capabilities-generator/))
 example:

 Setting capabilties for parallel execution in config/single.json
```
 {
  "user": "LambdaTest username",
  "key": "LambdaTest accesskey",

  "capabilities": {
    "build": "behave-test-lambdatest",
    "name": "YOUR TEST NAME"
  },

  "environments": [{
    "browser": "chrome"
  }]
}
```

### Run tests
##### Running tests
```bash
python behave_parallel.py -p 2    ( '-p 2' flag is used to specify the number of feature files you want to run in parallel)
```

## About LambdaTest

[LambdaTest](https://www.lambdatest.com/) is a cloud based selenium grid infrastructure that can help you run automated cross browser compatibility tests on 2000+ different browser and operating system environments. LambdaTest supports all programming languages and frameworks that are supported with Selenium, and have easy integrations with all popular CI/CD platforms. It's a perfect solution to bring your [selenium automation testing](https://www.lambdatest.com/selenium-automation) to cloud based infrastructure that not only helps you increase your test coverage over multiple desktop and mobile browsers, but also allows you to cut down your test execution time by running tests on parallel.
