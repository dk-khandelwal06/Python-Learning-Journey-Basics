function convertTemperature() {
    const name = document.getElementById('username').value;
    const temp = parseFloat(document.getElementById('temperature').value);
    const from = document.getElementById('from').value;
    const to = document.getElementById('to').value;
    let result = '';

    if (isNaN(temp)) {
        result = '❌ Please enter a valid temperature.';
    } else if (from === to) {
        result = `👋 Hey ${name || 'User'}, the temperature remains the same: ${temp} °${to}`;
    } else {
        let converted;

        // Convert temperature
        if (from === 'C') {
            if (to === 'F') converted = (temp * 9/5) + 32;
            if (to === 'K') converted = temp + 273.15;
        } else if (from === 'F') {
            if (to === 'C') converted = (temp - 32) * 5/9;
            if (to === 'K') converted = (temp - 32) * 5/9 + 273.15;
        } else if (from === 'K') {
            if (to === 'C') converted = temp - 273.15;
            if (to === 'F') converted = (temp - 273.15) * 9/5 + 32;
        }

        result = `✅ Hey ${name || 'User'}, the result is: <strong>${converted.toFixed(2)} °${to}</strong>`;
    }

    document.getElementById('result').innerHTML = result;
}

print()
print("Hello World")
print()

//         result = `✅ Hey ${name || 'Antagonist'}, the result is: <strong>${converted.toFixed(2)} °${to}</strong>`;
//     }

//     document.getElementById('result').innerHTML = result;
//   }
#include <iostream>
using namespace std;

int main() {

    return 0;
}
