# CHANGELOG

<!-- version list -->

## v0.7.1 (2026-11-08)

### Bug Fixes

- Text colour
  ([`897a4a7`](https://github.com/jayrickaby/run-7/commit/897a4a734a8c8fc891e1ab373a463d7389a8046a))

### Features

- Add 1px padding
  ([`679d7df`](https://github.com/jayrickaby/run-7/commit/679d7dfe9231a669e15d948c9685e019306ec19f))

- Add button padding
  ([`53e08bf`](https://github.com/jayrickaby/run-7/commit/53e08bfba47e8a5f727bfe9482f7370870bde5a0))

- Add padding to upper region
  ([`fe2d1f0`](https://github.com/jayrickaby/run-7/commit/fe2d1f0050d28870041798e958cb1d8374c4a39b))

- Add rectangle that uses the system base colour
  ([`61adf67`](https://github.com/jayrickaby/run-7/commit/61adf67ee416cad0e52038210dc9af85f84d6741))


## v0.7.0 (2026-11-07)

### Features

- If on kde, use kde theme
  ([`6f5c2a3`](https://github.com/jayrickaby/run-7/commit/6f5c2a3d9dcb6aeb6c05fabc447eda9563d8e4a6))

- Readd InstructionDialog from Frutiger7 repo
  ([`9ba7278`](https://github.com/jayrickaby/run-7/commit/9ba7278c67fa8b052ae66bb06ccaa332960e8cda))

- Remove external folder & frutiger7 references in qml
  ([`8036ad7`](https://github.com/jayrickaby/run-7/commit/8036ad7030272c2a925a4c638f7283940e1e86a1))

- Remove instances of 'textvcenteroffset'
  ([`b15b203`](https://github.com/jayrickaby/run-7/commit/b15b203a663e19a673ad408621e11c0f26182892))

- Remove instructiondialog and replace with messagedialog
  ([`41682a8`](https://github.com/jayrickaby/run-7/commit/41682a88cce08bbc2bb7230944a35c3b9892344f))

- Remove references a frutiger7 asset directory
  ([`4da2dc3`](https://github.com/jayrickaby/run-7/commit/4da2dc3783ad72676d75a98de5f3e1aad38ece67))

- Set style to 'org.kde.desktop' on kde
  ([`fc827bf`](https://github.com/jayrickaby/run-7/commit/fc827bf30313260eccb2a0054a3901cb3f585afe))

- Simplify build process
  ([`674f4ae`](https://github.com/jayrickaby/run-7/commit/674f4aec8f34b12e681dcfd4cfbeee7af3175f80))


## v0.6.0 (2026-07-20)

### Bug Fixes

- **config**: Fix location of build.sh in pyproject.toml
  ([`fa21442`](https://github.com/jayrickaby/run-7/commit/fa214429a4000ccd6ee9b01e02da2341d667851c))

### Features

- **backend**: Have script cleanup nuitka intermediatary build directories
  ([`84b4862`](https://github.com/jayrickaby/run-7/commit/84b4862fb8663b3e34b85f57f1d3fad48baea089))

- **config**: Cleanup and prepare project for nuitka building
  ([`a742b3a`](https://github.com/jayrickaby/run-7/commit/a742b3abadedd1bf8a336e6062d72f3a454c7251))

- **window**: Add return key shortcut to run action
  ([`1856a5e`](https://github.com/jayrickaby/run-7/commit/1856a5e91c9d8c5394c7da76063f709b4759c860))


## v0.5.0 (2026-07-13)

### Bug Fixes

- **backend**: Attempt to enforce local .ini files for settings on all OSes
  ([`2265906`](https://github.com/jayrickaby/run-7/commit/226590633b7286ac1eada7d27f78b579cd12e14b))

- **backend**: Change enforcement of ini format to before instantiation
  ([`6455a2b`](https://github.com/jayrickaby/run-7/commit/6455a2b10d1a4fe3503c8b62786f432fa2fbfbf1))

- **backend**: Change return type of processFilePath to be string
  ([`eb77e72`](https://github.com/jayrickaby/run-7/commit/eb77e72c44f9d0448e8e2848f2608800ba4c112f))

- **backend**: Sent browsed urls to backend to be processed to try and fix file browsing on windows
  ([`be8bd96`](https://github.com/jayrickaby/run-7/commit/be8bd96de4a8da32ce6204b4ef7d356b7b3beeda))

- **docs**: Update readme setup guide to reflect new repo name
  ([`24355c8`](https://github.com/jayrickaby/run-7/commit/24355c86779d55eeebbc396eb2f4a8aebe52a875))

### Features

- **docs**: Add config docs
  ([`ad46239`](https://github.com/jayrickaby/run-7/commit/ad4623983b4fc20550f16cf0c81a4462d1d1b6aa))


## v0.4.0 (2026-07-09)

### Bug Fixes

- **backend**: Adjust how application returns icon so that it doesn't break when trying to url the
  already-url
  ([`9e68cde`](https://github.com/jayrickaby/run-7/commit/9e68cde02a9e3ea39fdddb599ed0c1b864f2d278))

- **styling**: Restore appicon and add mipmaps
  ([`65f44d5`](https://github.com/jayrickaby/run-7/commit/65f44d543328e323371b79270e34ee3eb36824ef))

### Features

- **backend**: Add config
  ([`12a16a5`](https://github.com/jayrickaby/run-7/commit/12a16a56b8a4db951dd9532b7483e59d1cf57474))


## v0.3.0 (2026-07-09)

### Bug Fixes

- **backend**: Update main.py to reflect recent url changes
  ([`c41b0d8`](https://github.com/jayrickaby/run_7/commit/c41b0d8a4d9048883cf6815f536cf89f921f74d5))

- **backend**: Use qurl to get paths and then turn them to local files to fix missing assets on
  windows
  ([`09f9788`](https://github.com/jayrickaby/run_7/commit/09f9788ebaf34e6dfbde74ac160f3990e85794a6))

- **window**: Attempt to restore titlebar with more flags
  ([`8cf984a`](https://github.com/jayrickaby/run_7/commit/8cf984a425a767099c86c8222d4550be635947a0))

- **window**: Make sure pressing 'escape' on browse file dialogue doesnt close entire run window
  ([`4fc4afc`](https://github.com/jayrickaby/run_7/commit/4fc4afc55ab8f475d4ea014b24cc6f904675caeb))

- **window**: Use alternate method to disabling close action so that it is not visually affected
  ([`97d29bc`](https://github.com/jayrickaby/run_7/commit/97d29bcaee83041c5a6c72a828c5dbed16007c0a))

### Features

- **backend**: Add history
  ([`da8fa9d`](https://github.com/jayrickaby/run_7/commit/da8fa9dbafe829242ffc2ca8640b68b8c72cc509))

- **backend**: Add organisation / app details
  ([`e46169f`](https://github.com/jayrickaby/run_7/commit/e46169f1be544d9c12e0a9cd5e5854e328e91a40))

- **style**: Adjust app icon to be non-windows
  ([`97070ac`](https://github.com/jayrickaby/run_7/commit/97070aca8b8946d6c80035edaf3aeb7f0d92bbf2))

- **styling**: Update styling
  ([`9820afd`](https://github.com/jayrickaby/run_7/commit/9820afd67d60c4cb1b66d1dfd99138e69d9e275e))

- **window**: Make combobox text selected when window is focused
  ([`80d7ab9`](https://github.com/jayrickaby/run_7/commit/80d7ab98933bc33397d90b203b1179619e0b3275))


## v0.2.0 (2026-07-05)

### Features

- **backend**: Add desktop file name for Window Rules - Window class property
  ([`52d82cd`](https://github.com/jayrickaby/run_7/commit/52d82cd190f34470566b6d954c4e47ee146f5f06))

- **backend**: Add proper backend
  ([`579eca7`](https://github.com/jayrickaby/run_7/commit/579eca7b7dc5dc835ef1bf0d0a54cdeaa2aa7a89))


## v0.1.0 (2026-07-03)

- **styling**: Add elements and style with a frutiger aero theme
  ([`05c41e9`](https://github.com/jayrickaby/run_7/commit/05c41e969d31bff48b6aea48b507993068ae52fb))


## v0.0.0 (2026-06-30)

- Initial Release
