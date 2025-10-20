// Sample JavaScript code for testing code analysis patterns

// Potential security vulnerability - SQL injection
function getUserData(userId) {
    const query = "SELECT * FROM users WHERE id = " + userId; // Vulnerable
    return database.query(query);
}

// Performance issue - inefficient algorithm
function findDuplicates(array) {
    const duplicates = [];
    for (let i = 0; i < array.length; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] === array[j] && duplicates.indexOf(array[i]) === -1) {
                duplicates.push(array[i]);
            }
        }
    }
    return duplicates;
}

// Quality issue - unclear naming and no error handling
function calc(a, b, op) {
    if (op == "add") return a + b;
    if (op == "sub") return a - b;
    if (op == "mul") return a * b;
    if (op == "div") return a / b; // No division by zero check
}

// Better implementation examples
function getUserDataSecure(userId) {
    const query = "SELECT * FROM users WHERE id = ?";
    return database.prepare(query).run(userId);
}

function findDuplicatesEfficient(array) {
    const seen = new Set();
    const duplicates = new Set();
    
    for (const item of array) {
        if (seen.has(item)) {
            duplicates.add(item);
        } else {
            seen.add(item);
        }
    }
    
    return Array.from(duplicates);
}

function calculateWithValidation(operand1, operand2, operation) {
    if (typeof operand1 !== 'number' || typeof operand2 !== 'number') {
        throw new Error('Operands must be numbers');
    }
    
    switch (operation) {
        case 'add':
            return operand1 + operand2;
        case 'subtract':
            return operand1 - operand2;
        case 'multiply':
            return operand1 * operand2;
        case 'divide':
            if (operand2 === 0) {
                throw new Error('Division by zero is not allowed');
            }
            return operand1 / operand2;
        default:
            throw new Error(`Unsupported operation: ${operation}`);
    }
}