clusterdb = {};

async function fetch_cluster_db() {
    try {
        const response = await fetch("clusters.json");
        const json = await response.json()
        clusterdb = json;
    } catch (error) {
        console.error(error.message)
    }
}

function filter_clusters(clusters, keyword) {
    var ret = [];

    for (let i in clusters) {
        cluster = clusters[i];
        for (let site in cluster["thumbnails"]) {
            if (site.includes(keyword)) {
                ret.push(cluster);
                break;
            }
        }
    }

    return ret;
}

function cluster_to_tr(cluster, keyword) {
        var sites = Object.keys(cluster["thumbnails"]);
        var n_sites = sites.length;
        var thumbnail = "cluster_thumbnails/" + cluster["thumbnail"];

        var site_links = ""

        for (let i in sites) {
            domain = sites[i];

            if (keyword != "" && domain.includes(keyword)) {
                site_links += " " + `<b><a href="http://${domain}">${domain}</a></b>`;
            } else {
                site_links += " " + `<a href="http://${domain}">${domain}</a>`;
            }
        }

        row = document.createElement("tr");
        
        row.innerHTML = `
            <td>${cluster["id"]}</td>
            <td>${n_sites}</td>
            <td>${site_links}</td>
            <td><img src="${thumbnail}" /></td>
        `

        return row;
}

function refresh_cluster_list() {

    var table = document.getElementById("clustertable");
    table.innerHTML="";

    keyword = document.getElementById("filtertext").value;

    clusters = filter_clusters(clusterdb["clusters"], keyword);

    for (let i in clusterdb["clusters"]) {

        var cluster = clusters[i];

        row = cluster_to_tr(cluster, keyword);

        table.appendChild(row);

    }


}


document.addEventListener("DOMContentLoaded", (event) => {
    fetch_cluster_db().then( () => {
        console.log("Trying to do first load...");
        refresh_cluster_list();
    });
})


