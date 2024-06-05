/* Set fade time */
var fadeTime = 300;

/* Assign actions */
$(".product-quantity input").change(function () {
  updateQuantity(this);
});

$(".product-removal button").click(function () {
  removeItem(this);
});

/* Recalculate cart */
function recalculateCart() {
  var total = 0;

  /* Sum up row totals */
  $(".product").each(function () {
    var price = parseFloat($(this).children(".product-price").text());
    var quantity = parseInt($(this).find(".product-quantity input").val());
    var linePrice = price * quantity;
    total += linePrice;
  });

  /* Update totals display */
  $(".totals-value").fadeOut(fadeTime, function () {
    $("#cart-total").html(total.toFixed(2));
    if (total == 0) {
      $(".checkout").fadeOut(fadeTime);
    } else {
      $(".checkout").fadeIn(fadeTime);
    }
    $(".totals-value").fadeIn(fadeTime);
  });
}

/* Update quantity */
function updateQuantity(quantityInput) {
  /* Update line price display and recalc cart totals */
  var productRow = $(quantityInput).closest(".product");
  var price = parseFloat(productRow.children(".product-price").text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;

  productRow.find(".product-line-price").text(linePrice.toFixed(2));
  recalculateCart();
}

/* Remove item from cart */
function removeItem(removeButton) {
  /* Remove row from DOM and recalc cart total */
  var productRow = $(removeButton).closest(".product");
  productRow.slideUp(fadeTime, function () {
    productRow.remove();
    recalculateCart();
  });
}

// Initial call to calculate totals
recalculateCart();
