import axios from 'axios';

class HomeService {
    subject() {
        return axios.get(
            `${process.env.REACT_APP_API}/subjects`
        )
        .then(all => all.data)
        .catch(error => false)
    }
}

export default HomeService;