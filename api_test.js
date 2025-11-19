// fetch data from a public API
async function fetchData() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
}               
module.exports = { fetchData };

// test/api_test.js
const { fetchData } = require('../api_test');
const fetch = require('node-fetch');
jest.mock('node-fetch');
const { Response } = jest.requireActual('node-fetch');
describe('fetchData', () => {
    it('should fetch data from API', async () => {
        const mockData = { key: 'value' };
        fetch.mockReturnValue(Promise.resolve(new Response(JSON.stringify(mockData))));
        const data = await fetchData();
        expect(data).toEqual(mockData);
    });
    it('should handle fetch errors', async () => {

        fetch.mockReturnValue(Promise.reject(new Error('Fetch error')));
        await expect(fetchData()).rejects.toThrow('Fetch error');
    }
    );
}); 