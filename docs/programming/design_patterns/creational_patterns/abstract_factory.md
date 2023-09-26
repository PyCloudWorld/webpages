# Abstract Factory
![abstract_factory](images/abstract_factory.png)

## CODE
```python
from abc import ABC, abstractmethod

class AbstractMobileUIFactory(ABC):
	@abstractmethod
	def create_story(self):
		pass

	@abstractmethod
	def upload_photo(self):
		pass

class AndroidFactory(AbstractMobileUIFactory):
	def create_story(self):
		print("Inside AndroidFactory class")
		AndroidCreateStory().story()

	def upload_photo(self):
		print("Inside AndroidFactory class")
		AndroidUploadPhoto().photo()

class IosFactory(AbstractMobileUIFactory):
	def create_story(self):
		print("Inside IosFactory class")
		IosCreateStory().story()

	def upload_photo(self):
		print("Inside IosFactory class")
		IosUploadPhoto().photo()

class SymbianFactory(AbstractMobileUIFactory):
	def create_story(self):
		print("Inside SymbianFactory class")
		SymbianCreateStory().story()

	def upload_photo(self):
		print("Inside SymbianFactory class")
		SymbianUploadPhoto().photo()

class AbstractCreateStory(ABC):
	@abstractmethod
	def story(self):
		pass


class AndroidCreateStory(AbstractCreateStory):
	def story(self):
		print("[Android] Creating story on android platform.")

class IosCreateStory(AbstractCreateStory):
	def story(self):
		print("[IOS] Creating story on IOS platform.")

class SymbianCreateStory(AbstractCreateStory):
	def story(self):
		print("[Symbian] Ok boomer! Creating story on Symbian platform, while we can!!")


class AbstractUploadPhoto(ABC):
	@abstractmethod
	def photo(self):
		pass

class AndroidUploadPhoto(AbstractUploadPhoto):
	def photo(self):
		print("[Android] Uploading photo on android platform.")

class IosUploadPhoto(AbstractUploadPhoto):
	def photo(self):
		print("[IOS] Uploading photo on IOS platform.")

class SymbianUploadPhoto(AbstractUploadPhoto):
	def photo(self):
		print("[Symbian] So you want us to upload petroglyph? Since we are backward compatible, why not! Uploading photo on Symbian platform")

class Application():

	def get_factory(self, platform_type):
		factory = None
		if platform_type == "Android":
			factory = AndroidFactory()
		elif platform_type == "IOS":
			factory = IosFactory()
		elif platform_type == "Symbian":
			factory = SymbianFactory()
		else:
			print("ERROR: unknown platform type.")
		return factory

	def create_story(self, factory=None):
		if not factory:
			print("factory object not passed")
		factory.create_story()

	def upload_photo(self, factory=None):
		if not factory:
			print("factory object not passed")
		factory.upload_photo()

if __name__ == '__main__':
	app_object = Application()

	# in real world scenarios, instead of pass hardcoded platform type we can read platform type from config file.
	print("Running for Android platform...")
	factory_object = app_object.get_factory("Android")
	factory_object.create_story()
	factory_object.upload_photo()
	print("\n")

	print("Running for IOS platform...")
	factory_object = app_object.get_factory("IOS")
	factory_object.create_story()
	factory_object.upload_photo()
	print("\n")

	print("Running for Symbian platform...")
	factory_object = app_object.get_factory("Symbian")
	factory_object.create_story()
	factory_object.upload_photo()
	print("\n")
```


 Output.txt: Execution result
```bash
Running for Android platform...
Inside AndroidFactory class
[Android] Creating story on android platform.
Inside AndroidFactory class
[Android] Uploading photo on android platform.
Running for IOS platform...
Inside IosFactory class
[IOS] Creating story on IOS platform.
Inside IosFactory class
[IOS] Uploading photo on IOS platform.
Running for Symbian platform...
Inside SymbianFactory class
[Symbian] Ok boomer! Creating story on Symbian platform, while we can!!
Inside SymbianFactory class
[Symbian] So you want us to upload petroglyph? Since we are backward compatible, why not! Uploading photo on Symbian platform```
```

