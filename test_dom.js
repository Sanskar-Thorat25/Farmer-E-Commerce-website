const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const dom = new JSDOM(`
<!DOCTYPE html>
<html>
<body>
<table>
  <tbody id="cartTableBody">
      <tr>
          <td>Loading your cart...</td>
      </tr>
  </tbody>
</table>
<script>
    const tbody = document.getElementById('cartTableBody');
    tbody.innerHTML = '< tr > <td>Failed</td></tr >';
    console.log(tbody.innerHTML);
</script>
</body>
</html>
`, { runScripts: "dangerously" });
