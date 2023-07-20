# Testing, Compatibility and Validation
- [Manual Testing](#manual-testing)

- [Browser Compatibility](#browser-compatibility)

- [Validation and Performance](#validation-and-performance)


## Manual Testing

  ### Navbar
  | Action | Expected Behaviour | Pass/Fail |
  |--------|--------------------|-----------|
  | Select "Home" in Navigation bar | Renders Homepage | Pass |
  | Select "Add Recipie" in Navigation bar | Renders Add Recipie page | Pass |
  | Select "Register" in Navigation bar | Renders Register page | Pass |
  | Select "Login" in Navigation bar | Renders Login page | Pass |
  | Select "Logout" in Navigation bar | Renders Logout validation | Pass |
  | Select "Sign Out" button on "Logout" page | Logs out user and renders Homepage | Pass |
  | On "Register" page enter username and password values | Creates new site user | Pass |
  | On "Add Recipie" page enter values for "Title" and "Content", choose a category and select "Update" button  | Adds a new recipie rendered on Homepage | Pass |

  ### Home Page
  | Action | Expected Behaviour | Pass/Fail |
  |--------|--------------------|-----------|
  | Select a recipie to read content | Renders the recipie selected | Pass |

  ### Add Recipie Page
  | Action | Expected Behaviour | Pass/Fail |
  |--------|--------------------|-----------|
  | Add title | Title rendered when viewing recipie details | Pass |
  | Add content | Ingredients rendered when viewing recipie details | Pass |
  | Select category | Picture belonging to selected category rendered when viewing recipie details | Pass |
  | Select allergy | Allergy warning rendered when viewing recipie details | Pass |

  ### Update Recipie Page
  | Action | Expected Behaviour | Pass/Fail |
  |--------|--------------------|-----------|
  | Edit title | Updated title rendered when viewing recipie details | Pass |
  | Edit content | Updated ingredients rendered when viewing recipie details | Pass |
  | Edit category | Picture belonging to edited category rendered when viewing recipie details | Pass |
  | Select allergy | New allergy warning rendered when viewing recipie details | Pass |
  

## Browser Compatibility
 | Browser | Functionality for the following pages: Home, Add Recipie, Login, Logut, Register | Pass/Fail |
  |--------|--------------------|-----------|
  | Chrome | All functionality works as expected | Pass |
  | Safari | All functionality works as expected | Pass |
  | Firefox | All functionality works as expected | Pass |

## Validation and Performance

  ### Lighthouse
  <details>
  <summary>Desktop</summary>
  <br>
  
  - Home page

  [![Lightouse desktop Home page](assets/images/home_desktop.png)]

  - View Recipie Detauls page

  [![Lightouse desktop View Recipie page](assets/images/view_recipie_desktop.png)]

  - Add Recipie page

  [![Lightouse Add Recipie desktop page](assets/images/addrecipie_desktop.png)]

  - Update page

  [![Lightouse Add Recipie desktop Page](assets/images/update_desktop.png)]

  - Register page

  [![Lightouse Register desktop Page](assets/images/register_desktop.png)]

  - Login

  [![Lightouse Login desktop Page](assets/images/login_desktop.png)]

  - Logout

  [![Lightouse Logout desktop page](assets/images/logout_desktop.png)]

 </details>

  <details>
  <summary>Mobile</summary>
  <br>
  
  Home page
  [![Lightouse desktop Home page](assets/images/home_mobile.png)]

  View Recipie Details page
  [![Lightouse desktop View Recipie page](assets/images/view_recipie_mobile.png)]

  - Add Recipie page

  [![Lightouse Add Recipie desktop page](assets/images/addrecipie_mobile.png)]

  - Update page

  [![Lightouse Add Recipie desktop Page](assets/images/update_mobile.png)]

  - Register page

  [![Lightouse Register desktop Page](assets/images/register_mobile.png)]

  - Login
  
  [![Lightouse Login desktop Page](assets/images/login_mobile.png)]

  - Logout

  [![Lightouse Logout desktop page](assets/images/logout_mobile.png)]

  </details>

### HTML Validation
 HTML validation was carried out using [W3 NU HTML Checker](https://validator.w3.org/nu/).
  [![W3 NU HTML Checker](assets/images/html_checker.png)]

### CSS Validation
 CSS validation was carried out using [W3C CSS Validator Checker](https://jigsaw.w3.org/css-validator/).
  [![W3C CSS Validator Checker](assets/images/css_checker.png)]

### JavaScript Validation
 JavaCript validation was carried out using [jshint](https://jshint.com/)
  [![JavaScript validation with jshint](assets/images/jshint.png)]

### Python Validation

  <details>
  <summary>Python Validation</summary>
  <br>

  | .py file | CI Python Linter Result|
  |--------|--------------------|
  | settings.py | [![settings.py Python Linter result screenshot](assets/images/settings.py_python_linter.png)] |
  
  </details> 
  


  To test 
  ### HTML, CSS and Python validation
  ### Lighthouse
  ### W3C Validation 
  ### Python Validation