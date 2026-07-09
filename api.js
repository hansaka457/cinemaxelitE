const API_BASE = 'http://localhost:5000/api'; // Deploy උනාට පස්සේ මේක මාරු කරනවා

async function fetchOmdbData(imdbID) {
    try {
        const res = await fetch(`${API_BASE}/omdb?i=${imdbID}`);
        const json = await res.json();
        return json.success ? json.data : null;
    } catch (e) {
        console.error(e);
        return null;
    }
}

async function fetchVideoData(imdbID) {
    try {
        const res = await fetch(`${API_BASE}/video/${imdbID}`);
        const json = await res.json();
        return json.success ? json.data : null;
    } catch (e) {
        console.error(e);
        return null;
    }
}

async function searchMovies(query) {
    try {
        const res = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}`);
        const json = await res.json();
        return json.success ? json.data : [];
    } catch (e) {
        console.error(e);
        return [];
    }
}
