import axios from '../axiosCustom';

const UserAPI =  {

    /**
     * User Login API:<br/>
     * OnSuccess: Retrieves new JWT & stores in localstorage <br/>
     * OnFail: Returns Error and message
     * @param credentials
     * @returns {Promise<response<any>|Error>}
     */
    login: async function(credentials)  {
        try {
            const res = await axios.post('/login', credentials);
            console.log('Response Headers:', res.headers); // This should log all headers
            if(res.status===200) {
                const token = res.headers['authorization'] || res.headers['Authorization'];
                console.log('Authorization Header:', token); // This should log the token
                if (token) {
                    localStorage.setItem(process.env.REACT_APP_TOKEN_NAME, token);
                }
                return res;
            } else {
                throw new Error('Login response was not OK.');
            }
            }catch (e){
            if (e.response.status === 403 ) return new Error('Invalid Credentials');
            else return new Error('Oops! We\'re checking what the problem is.')
        }
    
    },
    create: async function (userDetails) {
        try {
            return await axios.post('/api/users/registration', userDetails)
        } catch (e) {
            const errorMsg = e?.response?.data[0] || e.message()
            return new Error(errorMsg)
        }
    },
    getUsers: async function (pageable) {
        try{
            return await axios.get('/api/users', {params: pageable})
        }catch (e){
            console.error(e.response)
        }
    },

    getUserById: async function(userId) {
        try{
            return await axios.get(`/api/users/${userId}`)
        }catch (e) {
            console.error(e.response)
        }
    }
}

export default UserAPI;
