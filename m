<!DOCTYPE html>
<html>
<head><title>Search</title></head>
<body>
  <h2>Search Results for: </h2>
  <div id="results"></div>

  <script>
    // Unsafe: directly writing user input to the DOM
    const params = new URLSearchParams(window.location.search);
    const query = params.get("q");
    document.getElementById("results").innerHTML = query;
  </script>
</body>
</html>
